from typing import Optional, List, Any
import json


def extract_first_json(have_json) -> tuple[str, int]:
    """
    Extract first likely json. (ex. {}, {"this_is": "json"} , {not json} )

    :param have_json: likely json string
    :return: (extract json string, last index of json)
    """
    braces_start_cnt = 0
    braces_end_cnt = 0
    braces_start_index: int = have_json.find("{")

    if have_json.find("{") > -1:
        for i in range(len(have_json)):
            if have_json[i] == "{":
                braces_start_cnt += 1
            elif have_json[i] == "}" and i > braces_start_index:
                # braces_start_index より上という制約をつけないと "} hoge: {}" の最初もカウントされる
                braces_end_cnt += 1
            else:
                continue

            if (braces_start_cnt >= 1 and braces_start_cnt == braces_end_cnt):
                return (have_json[braces_start_index:i + 1], i)
    return ("", -1)


def extract_all_json(have_json: str):
    """
    Extract all likely json.

    :param have_json: string may have JSON
    :return: Extract all (likely) json (  ["{}", "{'aa':'bb'}", "{not json}"]  )
    """
    result = []
    MAX_LOOP = 200
    cnt = 0
    while 1:
        (extracted, end_index) = extract_first_json(have_json)
        if extracted != "":
            result.append(extracted)
            have_json = have_json[end_index:]
        elif extracted == "":
            return result

        cnt += 1
        if (MAX_LOOP < cnt):
            return result


def convert_jsons(jsons: List[str]) -> List[Any]:
    result = []
    for j in jsons:
        converted_json = str2json(j)
        if converted_json != None:
            result.append(converted_json)
    return result


def flatten_json(j):
    out = {}
    def flatten(keys, name=''):
        if type(keys) is dict:
            for k in keys:
                flatten(keys[k], name + k + '_')
        elif type(keys) is list:
            index = 0
            for k in keys:
                flatten(k, name + str(index) + '_')
                index += 1
        else:
            out[name[:-1]] = keys

    flatten(j)
    return out


def str2json(json: str) -> Optional[str]:
    try:
        return json.loads(str)
    except:
        return None


def test_extract_json():
    assert (extract_first_json("012{456}89") == ("{456}", 7))
    assert (extract_first_json("012}}56{{9") == ("", -1))
    assert (extract_first_json("012{{56}}9") == ("{{56}}", 8))


def test_extract_all_json():
    actual = extract_all_json("}{}}}aaa: {}},} bbb: {'aaa' : 123, ddd: []}")
    expect = ["{}", "{}", "{'aaa' : 123, ddd: []}"]
    assert (actual == expect)
