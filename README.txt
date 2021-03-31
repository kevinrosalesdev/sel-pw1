Structure & Contents of the ZIP File [RULES]
================================================================================================

- Documentation/
    * report.pdf: Report of the project containing the requested information such as
                  pseudo-code, evaluation of results, instructions on how to execute the code...

- Data/
    * lenses.csv: Test dataset used in the course slides.
    * ecoli.csv: Small numerical dataset.
    * car.csv: Medium categorical dataset.
    * rice.csv: Large numerical dataset.
    * stroke.csv: Large mixed dataset.

- Out/
    * lenses_rules.out: Human-readable rules from Lenses dataset.
    * ecoli_rules.out: Human-readable rules from Ecoli dataset.
    * car_rules.out: Human-readable rules from Car dataset.
    * rice_rules.out: Human-readable rules from Rice dataset.
    * stroke_rules.out: Human-readable rules from Stroke dataset.

- Source/
    - datapreprocessor/
        - preprocessor.py: Loads and preprocesses the data from the datasets.
    - rulesmanager/
        - generator.py: Generates the rules.
        - interpreter.py: Interprets the rules.
    - utils/
        - metrics.py: Measures the quality of the results.
        - plotter.py: Writes the rules in a file in a human-readable way.

- main.py: Executable file. Plots the results of applying RULES to each dataset.

- README.txt: this file.