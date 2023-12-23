import pandas as pd
from process_nitta import RamanSample


def test_raman():
    sample = RamanSample(
        file_path="./process-nitta/sample_data/raman.txt",
        name="sample",
    )
    result_df = sample.get_result_df()
    answer_df = pd.read_csv("./process-nitta/tests/answer_data/raman.csv", index_col=0)
    pd.testing.assert_frame_equal(result_df, answer_df)
