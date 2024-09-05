from render_quarto import render_quarto
import os

render_quarto(
    input_file = "quarto_reports/report_test.qmd",
    video_path = os.path.abspath("test_video.mp4"),
    output_dir = "report_folder"
)