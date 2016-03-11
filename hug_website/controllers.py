from blox.compile import filename
from blox.text import Text


def frame(data, template=filename('hug_website/views/frame.shpaml')):
    ui = template()
    ui.version.text = data['version']
    ui.main_content(globals()[data['page']](data['content']))
    return ui


def home(data, template=filename('hug_website/views/home.shpaml')):
    ui = template()
    ui.slogan.text = data['slogan']
    ui.introduction.text = data['introduction']
    ui.example_header.text = data['example_header']
    ui.performance_header.text = data['performance_header']
    ui.performance_description.text = data['performance_description']
    ui.versioning_header.text = data['versioning_header']
    ui.versioning_description.text = data['versioning_description']
    ui.documentation_header.text = data['documentation_header']
    ui.documentation_description.text = data['documentation_description']
    ui.annotation_header.text = data['annotation_header']
    ui.annotation_description.text = data['annotation_description']
    ui.reuse_header.text = data['reuse_header']
    ui.reuse_description.text = data['reuse_description']
    ui.get_started_header.text = data['get_started_header']
    ui.get_started_description.text = data['get_started_description']
    return ui
