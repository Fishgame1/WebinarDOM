import os
import time
from pathlib import Path

from Engine.open_leocode import OpenLeocode

cwd = str(Path(__file__).parents[1])
os.chdir(cwd)


def test_upload_cv_to_qa_team():
    with OpenLeocode() as main_page:
        careers = main_page.careers()
        time.sleep(2)
        careers.see_all()
        time.sleep(1)
        cv_upload = careers.get_job_offer_by_number(6).apply()
        time.sleep(1)
        cv_upload.write_name('Mike')
        cv_upload.write_email('Mike')
        cv_upload.write_last_name('Mikelson')
        cv_upload.write_phone('0000000000')
        cv_upload.upload_cv(os.path.join(cwd, 'Tests/CV.pdf'))
        cv_upload.apply()
