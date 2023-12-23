import pandas as pd
from process_nitta import IRNICOLETSample


def test_ir():
    sample = IRNICOLETSample(
        file_path="./process-nitta/sample_data/ir.csv",
        name="sample",
    )
    result_df = sample.get_result_df()
    answer_df = pd.read_csv("./process-nitta/tests/answer_data/ir.csv", index_col=0)
    pd.testing.assert_frame_equal(result_df, answer_df)
