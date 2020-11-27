def extract_json(have_json) -> tuple(str, int):
    braces_start_cnt = 0
    braces_end_cnt = 0
    braces_start_index: int = have_json.find("{")

    if have_json.find("{") > -1:
        for i in range(len(have_json[braces_start_index:])):
            if have_json[i] == "{":
                braces_start_cnt += 1
            elif have_json[i] == "}":
                braces_end_cnt += 1
            else:
                continue

            if(braces_start_cnt >= 1 and braces_start_cnt == braces_end_cnt):
                return (have_json[braces_start_index:i+1], int)
    return ("", -1)

def recursive_extract_json(have_json: str):
    result = []
    have_json
    pass

def test_extract_json():
    assert (extract_json("aaa{bbb}aaa") == ("{bbb}", -1) )
    assert (extract_json("aaa{{bbb}}aaa") == ("{{bbb}}", -1) )
    assert (extract_json("aaa}}aaa{{aaa") == ("", -1) )