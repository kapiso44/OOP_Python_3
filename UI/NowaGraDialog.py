from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QFormLayout, QVBoxLayout, \
    QHBoxLayout, QGroupBox, QDialogButtonBox, QLabel, QSlider


class Suwak:

    def __init__(self, label, initial_value=15, _min=1, _max=50, increment=5):
        self.label = label
        self.increment = increment
        self.widget = QWidget()
        self.slider = QSlider(self.widget)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setMinimum(_min)
        self.slider.setMaximum(_max)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setValue(initial_value)
        self.slider.setSingleStep(increment)
        self.slider.setTickInterval(increment)
        self.slider_label = QLabel(self.widget)
        self.slider_label.setText(str(initial_value))
        layout = QHBoxLayout(self.widget)
        layout.addWidget(self.slider)
        layout.addWidget(self.slider_label)
        self.slider.valueChanged.connect(lambda value: self.slider_label.setText(str(value)))

    def get_label(self):
        return self.label

    def get_widget(self):
        return self.widget

    def get_value(self):
        return self.slider.value()


class NowaGraDialog(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Nowa gra")
        self.verticalLayout = QVBoxLayout(self)
        self.groupBox = QGroupBox("Tworzenie nowego świata", self)
        self.formLayout = QFormLayout(self.groupBox)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.buttonBox.accepted.connect(lambda: self.exit_dialog(True))
        self.buttonBox.rejected.connect(lambda: self.exit_dialog(False))

        self.input_list = [Suwak('Podaj wysokość'), Suwak('Podaj szerokość'),
                           Suwak('Podaj zagęszczenie w %', 20, 0, 100, 10)]

        for position, input_obj in enumerate(self.input_list):
            label = QLabel(self.groupBox)
            label.setText(input_obj.get_label())
            self.formLayout.setWidget(position, QFormLayout.LabelRole, label)
            input_field = input_obj.get_widget()
            self.formLayout.setWidget(position, QFormLayout.FieldRole, input_field)

        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.buttonBox)

        self.resize(self.verticalLayout.sizeHint())

        self.output = []
        self.accepted = False
        self.setModal(True)

    def exit_dialog(self, _accepted):
        self.accepted = _accepted
        self.close()

    def closeEvent(self, event):
        for input_obj in self.input_list:
            self.output.append(input_obj.get_value())
