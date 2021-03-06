from .keyboard_control import parse_command_line_arguments
from .keyboard_control import control_microscope_with_keyboard
from .utilities.recalibrate import generate_lens_shading_table_closed_loop
import argparse

def main():
    parser = argparse.ArgumentParser(description="Control an Openflexure Microscope")
    parser.add_argument("--recalibrate", action="store_true", 
            help="Reset the microscope's settings and regenerate the lens shading correction table.  Saves to ./microscope_settings.npz.")
    parser.add_argument("--no_stage", action="store_true", 
            help="Do not attempt to connect to a motor controller.  Use this option if you are moving the microscope by hand.")
    parser.add_argument("--output", help="directory or filepath (with %%d wildcard) for saved images", default="~/Desktop/images")
    parser.add_argument("--settings_file", help="File where the microscope settings are stored.", default="microscope_settings.npz")
    args = parser.parse_args()
    if args.recalibrate:
        generate_lens_shading_table_closed_loop(args.settings_file)
    else:
        control_microscope_with_keyboard(output=args.output, dummy_stage=args.no_stage, settings_file=args.settings_file)

if __name__ == '__main__':
    main()

