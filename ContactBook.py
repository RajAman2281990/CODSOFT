import PySimpleGUI as sg


layout = [
    [sg.TabGroup([
        [sg.Tab("Add / Edit Contact", [
            [sg.Text("Name"), sg.InputText(key='name')],
            [sg.Text("Phone Number"), sg.InputText(key='phone')],
            [sg.Text("Email"), sg.InputText(key='email')],
            [sg.Text("Address"), sg.InputText(key='address')],
            [sg.Button("Add", key='add', button_color=('white', 'blue')),
             sg.Button("Edit", key='edit', button_color=('white', 'blue')),
             sg.Button("Update", key='update', button_color=('white', 'blue')),
             sg.Button("Delete", key='delete', button_color=('white', 'blue'))
            ]
        ]),
        sg.Tab("Search Contact", [
            [sg.Text("Name"), sg.InputText(key='search_name')],
            [sg.Button("Search", key='search', button_color=('white', 'blue'))],
            [sg.Text("", size=(25, 1), key='search_result')],
            [sg.Multiline("", size=(40, 6), key='contact_details', disabled=True, autoscroll=True)]
        ])
        ]]
    )],
    [sg.Listbox(values=[], size=(40, 10), key='contact_list')],
    [sg.Button("Exit", key='exit', button_color=('white', 'red'), size=(10, 1))]
]


window = sg.Window("Contact Book", layout, finalize=True)

contacts = []


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'exit':
        break

    if event == 'add':
        contact = {
            'Name': values['name'],
            'Phone Number': values['phone'],
            'Email': values['email'],
            'Address': values['address'],
        }
        contacts.append(contact)
        window['contact_list'].update(values=[contact['Name'] for contact in contacts])
        sg.popup('Contact added successfully!')
        window['name'].update('')
        window['phone'].update('')
        window['email'].update('')
        window['address'].update('')

    if event == 'edit':
        selected_contact = window['contact_list'].get()
        if selected_contact:
            selected_contact = selected_contact[0]
            for i, contact in enumerate(contacts):
                if contact['Name'] == selected_contact:
                    contacts[i] = {
                        'Name': values['name'],
                        'Phone Number': values['phone'],
                        'Email': values['email'],
                        'Address': values['address'],
                    }
                    window['contact_list'].update(values=[contact['Name'] for contact in contacts])
                    sg.popup('Contact updated successfully!')
                    break
        else:
            sg.popup('Please select a contact from the list.')

    if event == 'update':
        selected_contact = window['contact_list'].get()
        if selected_contact:
            selected_contact = selected_contact[0]
            for i, contact in enumerate(contacts):
                if contact['Name'] == selected_contact:
                    values['name'] = contact['Name']
                    values['phone'] = contact['Phone Number']
                    values['email'] = contact['Email']
                    values['address'] = contact['Address']
                    sg.popup('Contact details populated for editing.')
                    break
        else:
            sg.popup('Please select a contact from the list.')

    if event == 'delete':
        selected_contact = window['contact_list'].get()
        if selected_contact:
            selected_contact = selected_contact[0]
            for contact in contacts:
                if contact['Name'] == selected_contact:
                    contacts.remove(contact)
                    window['contact_list'].update(values=[contact['Name'] for contact in contacts])
                    sg.popup('Contact deleted successfully!')
                    break
        else:
            sg.popup('Please select a contact from the list.')

    if event == 'search':
        search_name = values['search_name']
        found_contact = None
        for contact in contacts:
            if contact['Name'] == search_name:
                found_contact = contact
                break
        if found_contact:
            result_text = f"Name: {found_contact['Name']}\nPhone: {found_contact['Phone Number']}\nEmail: {found_contact['Email']}\nAddress: {found_contact['Address']}"
            window['search_result'].update('Contact found:')
            window['contact_details'].update(result_text)
        else:
            window['search_result'].update('Contact not found:')
            window['contact_details'].update('')

    if event == 'change_theme':
        selected_theme = values['theme_combo']
        sg.theme(selected_theme)

window.close()
