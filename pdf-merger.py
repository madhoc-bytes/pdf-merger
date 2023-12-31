import PySimpleGUI as sg
from PyPDF2 import PdfMerger

def merge_pdf_files(output_path, files):
    merger = PdfMerger()

    for file in files:
        merger.append(file)

    merger.write(output_path)
    merger.close()

def main():
    layout = [
        [sg.Text('Select PDF files to merge:', font='Any 12')],
        [sg.InputText('', key='-FILE-', enable_events=True, readonly=True), sg.FilesBrowse()],
        [sg.Listbox([], size=(50, 6), key='-FILE LIST-')],
        [sg.Button('Merge', key='-MERGE-'), sg.Button('Clear', key='-CLEAR-'), sg.Exit()]
    ]

    window = sg.Window('PDF Merger', layout)

    files_to_merge = []

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        if event == '-FILE-':
            files = values['-FILE-'].split(';')
            for file in files:
                if file not in files_to_merge:
                    files_to_merge.append(file)
            window['-FILE LIST-'].update(files_to_merge)

        if event == '-MERGE-':
            output_file = sg.popup_get_file('Save merged PDF as:', save_as=True, file_types=(('PDF Files', '*.pdf'),))
            if output_file:
                output_file += '.pdf'
                merge_pdf_files(output_file, files_to_merge)
                sg.popup('PDF files merged successfully!', title='Success')
                files_to_merge.clear()
                window['-FILE LIST-'].update(files_to_merge)

        if event == '-CLEAR-':
            files_to_merge.clear()
            window['-FILE LIST-'].update(files_to_merge)

    window.close()

if __name__ == '__main__':
    main()
