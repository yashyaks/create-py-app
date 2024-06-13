import os
import shutil
import click

@click.group()
def cli():
    pass

def copy_template(template_name, project_name):
    template_path = os.path.join(os.path.dirname(__file__), 'templates', template_name)
    target_path = os.path.join(os.getcwd(), project_name)
    
    if os.path.exists(target_path):
        click.echo(f'Error: Directory {project_name} already exists.')
        return
    
    try:
        shutil.copytree(template_path, target_path)
        click.echo(f'{template_name} project created successfully at {target_path}')
    except Exception as e:
        click.echo(f'Error: {e}')

@click.command()
@click.option('--framework', prompt='Select a framework: \n 1. Supervised Learning \n 2. Streamlit App \n 3. Flask App\n', 
              type=click.Choice(['1', '2', '3']), help='The type of project to create.')
@click.argument('project_name')
def create_project(framework, project_name):
    framework_mapping = {
        '1': 'supervised_learning',
        '2': 'streamlit_app',
        '3': 'flask_app'
    }
    
    template_name = framework_mapping[framework]
    copy_template(template_name, project_name)

cli.add_command(create_project,name="create_project")

if __name__ == '__main__':
    cli()
