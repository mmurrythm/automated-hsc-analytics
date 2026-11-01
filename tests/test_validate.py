import pandas as pd
from hsc_analytics.validate import normalize_and_validate

def test_rates_and_consistency():
    df = pd.DataFrame([{"board_code":"dhaka","college_name":"Test","eiin":123456,
                        "appeared":100,"passed":80,"failed":20,"gpa5_count":10}])
    out = normalize_and_validate(df)
    assert round(float(out.iloc[0]["pass_rate"]), 2) == 80.00
    assert round(float(out.iloc[0]["gpa5_rate"]), 2) == 10.00
    assert out.iloc[0]["validation_flags"] == ""
