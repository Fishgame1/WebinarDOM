import os
import time
from pathlib import Path

from Engine.open_leocode import OpenLeocode

cwd = str(Path(__file__).parents[1])
os.chdir(cwd)


def test_upload_cv_to_qa_team():
    with OpenLeocode() as main_page:
        careers = main_page.careers()
        time.sleep(1)
        cv_upload = careers.get_job_offer_by_number(1).apply()
        time.sleep(1)
        cv_upload.write_name('Mike')
        cv_upload.write_email('Mikelson')
        cv_upload.write_about_your_self("I'm so happy that so many people is watching this!")
        cv_upload.upload_cv(os.path.join(cwd, 'Tests/CV.pdf'))
        cv_upload.apply()
        time.sleep(5)
        print('wait here!')
