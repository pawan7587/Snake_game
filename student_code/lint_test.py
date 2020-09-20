from pylint.lint import Run
Results = Run(["snake_class.py"], do_exit=False)
print(Results.linter.stats["global_note"])