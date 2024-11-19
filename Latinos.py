import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7700434658:AAEJetoOm9YYVok3EKYOQgAMNKRszqkjfpA"
bot = telebot.TeleBot(TOKEN)

# Lista para almacenar los IDs de los mensajes secundarios
tracked_messages = []

# Manejo del comando /start
@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "¡Hola, amigo!! ¿En qué puedo ayudarte hoy?")
    show_main_menu(chat_id)

# Menú principal con botones
def show_main_menu(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📚 Tramites migratorios", callback_data="info_academica"))
    markup.add(InlineKeyboardButton("📍 Direcciones", callback_data="direcciones"))
    markup.add(InlineKeyboardButton("🎓 Becas y ayudas", callback_data="becas"))
    markup.add(InlineKeyboardButton("📅 Eventos y actividades", callback_data="eventos"))
    markup.add(InlineKeyboardButton("🙏 Donaciones", callback_data="donaciones"))
    markup.add(InlineKeyboardButton("💬 Soporte y asesoría", callback_data="soporte"))
    bot.send_message(chat_id, "Selecciona una opción del menú:", reply_markup=markup)

# Función que se llama cuando se presiona un botón
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global tracked_messages  # Accedemos a la lista global

    chat_id = call.message.chat.id

    # Manejamos los datos del callback
    if call.data == "info_academica":
        bot.answer_callback_query(call.id, "Seleccionaste Trámites migratorios...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        show_visa_options(chat_id)


    
    elif call.data == "direcciones":
        bot.answer_callback_query(call.id, "Seleccionaste Direcciones...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        show_direcciones_options(chat_id)


    elif call.data == "dormitorios":
        bot.answer_callback_query(call.id, "Seleccionaste Dormitorios...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        show_dormitory_options(chat_id)


    elif call.data == "dorm1":
        bot.answer_callback_query(call.id, "Seleccionaste Dormitorio 1...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        msg = bot.send_message(chat_id, 
                               "ул. Большакова, 79\n"
                               "Jefa del Dormitorio: Elena Valerievna Arkhipova\n"
                               "Presidente: [Anastasia Botina](https://vk.com/example_profile)", parse_mode="Markdown")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)
    
    elif call.data == "dorm2":
        bot.answer_callback_query(call.id, "Seleccionaste Dormitorio 2...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        msg = bot.send_message(chat_id, 
                               "ул. Большакова, 77\n"
                               "Jefa del Dormitorio: Давыдова Анна Михайловна\n"
                               "Presidente: [Анастасия Смородина](https://vk.com/satella_23)", parse_mode="Markdown")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)


    elif call.data == "dorm5":
        bot.answer_callback_query(call.id, "Seleccionaste Dormitorio 5...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        msg = bot.send_message(chat_id, 
                               "ул. Большакова, 77\n"
                               "Jefa del Dormitorio: Минязева Гульнара Раисовна\n"
                               "Presidente: [Анастасия Петрова](https://vk.com/sttaceyy)", parse_mode="Markdown")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)

    elif call.data == "dorm7":
        bot.answer_callback_query(call.id, "Seleccionaste Dormitorio 7...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        msg = bot.send_message(chat_id, "7")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)


    elif call.data == "dorm8":
        bot.answer_callback_query(call.id, "Seleccionaste Dormitorio 8...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        msg = bot.send_message(chat_id, 
                               "ул. Комсомольская, 70\n"
                               "Jefa del Dormitorio: Наталья Сергеевна Братчикова\n"
                               "Presidente: [Мошечкова Любовь](https://vk.com/id249044204)", parse_mode="Markdown")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)


    elif call.data == "dorm15":
        bot.answer_callback_query(call.id, "Seleccionaste Dormitorio 15...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        msg = bot.send_message(chat_id, 
                               "ул. Коминтерна, 11\n"
                               "Jefa del Dormitorio: Чернышова Надежда Ивановна\n")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)


    elif call.data == "nvk1":
        bot.answer_callback_query(call.id, "Seleccionaste Dormitorio NKK 1...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        msg = bot.send_message(chat_id, 
                               "ул. 100 летия Уральского университета, 6\n"
                               "Jefa del Dormitorio: Азанова Светлана Аркадьевна\n"
                               "Presidente: [Вероника Барсукова](https://vk.com/your_littlelove)", parse_mode="Markdown")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)


    elif call.data == "nvk2":
        bot.answer_callback_query(call.id, "Seleccionaste Dormitorio NVK 2...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        msg = bot.send_message(chat_id, 
                               "ул. 100 летия Уральского университета, 6\n"
                               "Jefa del Dormitorio: Толшина Марина Геннадьевна\n"
                               "Presidente: [Вероника Барсукова](https://vk.com/your_littlelove)", parse_mode="Markdown")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)

   
    elif call.data == "becas":
        bot.answer_callback_query(call.id, "Seleccionaste Becas y ayudas...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        msg = bot.send_message(chat_id, "Publicaremos algo si hay algun intercambio academico, becas e incluso ofertas de trabajo")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)


    elif call.data == "eventos":
        bot.answer_callback_query(call.id, "Seleccionaste Eventos y actividades...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        msg = bot.send_message(chat_id, "Aqui se publicaran todos los eventos de la comunidad, de otras comunidades y de la universidad")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)

    elif call.data == "donaciones":
        bot.answer_callback_query(call.id, "Seleccionaste Donaciones...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        show_donations_options(chat_id)


    elif call.data == "soporte":
        bot.answer_callback_query(call.id, "Seleccionaste Soporte y asesoría...")
        remove_message(chat_id, call.message.message_id)  # Eliminar el mensaje del menú principal
        msg = bot.send_message(chat_id, "¿Necesitas ayuda? Contáctame:\n\n- Email: jeremmymolina274@gmail.com\n- Teléfono: +7 932 614 99 72\n- Telegram: @Cherrjma")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)

    # Opciones dentro del submenú de visado
    elif call.data == "primera_visa":
        bot.answer_callback_query(call.id, "Mostrando información sobre la primera visa...")
        msg = bot.send_message(chat_id, 
            "- 2 copias del pasaporte (primera página)\n"
            "- 1 copia de todas las páginas del pasaporte (páginas con sellos)\n"
            "- 2 copias de la carta de migración\n"
            "- 2 copias de la visa con la que ingresaron al país\n"
            "- 2 copias de la registración\n"
            "- 1 foto tamaño carnet\n"
            "- Pago de 1900 p por la visa\n"
            "- Copia del contrato de estudios\n"
            "- Original y copias de exámenes médicos (VIH, Narcóticos y Radiografía)")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)

    elif call.data == "prolongacion_visa":
        bot.answer_callback_query(call.id, "Mostrando información sobre prolongación de visa...")
        msg = bot.send_message(chat_id, 
            "- 2 copias del pasaporte (primera página)\n"
            "- 1 copia de todas las páginas del pasaporte (páginas con sellos)\n"
            "- 2 copias de la carta de migración\n"
            "- 2 copias de la visa anterior\n"
            "- 2 copias de la registración\n"
            "- 1 foto tamaño carnet\n"
            "- Pago de 1900 p por la visa\n"
            "- Copia y original de la tarjeta verde\n"
            "- Copia del contrato de estudios\n"
            "- Original y copias de exámenes médicos (VIH, Narcóticos y Radiografía)\n"
            "\n*Los examenes medigos se pueden hacer en ул. ясная 46 y ул. Сыромолотова 19*", parse_mode="Markdown")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)

    elif call.data == "registracion":
        bot.answer_callback_query(call.id, "Mostrando información sobre registración...")
        msg = bot.send_message(chat_id, 
            "- Contrato original del dormitorio\n"
            "- Copia de todas las paginas llenas del pasaporte\n"
            "- Copia de la cartera de migracion\n"
            "- ***Copia de la registracion anterior\n"
            "- ***Copia de la tarjeta verde\n"
            "- ***Copias de los examenes medicos (VIH, Narcoticos y rayos X)\n\n\n"
            "*** Significa que solo es para segunda registracion en adelante")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)

    elif call.data == "tarjeta-verde":
        bot.answer_callback_query(call.id, "Mostrando información sobre la tarjeta verde...")
        msg = bot.send_message(chat_id,
                               "Este proceso se realiza una sola vez por la policia de tu region, el documento no tiene caducidad y sirve en todo el territorio de la Federacion Rusa\n"
                               "Los documentos necesarios son los siguientes:\n"
                               "\t  - Copias de los examenes medicos (VIH, Narcoticos y rayos X)\n"
                               "\t  - Pasaporte y traduccion del mismo con firma de un notario\n"
                               "\t  - Registracion\n"
                               "\t  - Carta de migracion\n"
                               "\t  - Copia y original de la visa actual\n")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)
    
    elif call.data == "institutos":
        bot.answer_callback_query(call.id, "Mostrando información sobre institutos...")
        msg = bot.send_message(chat_id, 
            "*-  Ciencias Naturales y Matemáticas*\n\t\t\t📍Ул. Куйбышева, 48\n"
            "*-  Nuevos Materiales y Tecnologías*\n\t\t\t📍Ул. Мира, 28\n"
            "*-  Radioelectrónica y Tecnologías de la Información*\n\t\t\t📍Ул. Мира, 32\n"
            "*-  Construcción y Arquitectura*\n\t\t\t📍Ул. Мира, 17\n"
            "*-  Cultura Física, Deportes y Política Juvenil*\n\t\t\t📍Ул. Коминтерна, 14\n"
            "*-  Economía y Gestión*\n\t\t\t📍Ул. Мира, 19, ул. Ленина, 13б, ул. Гоголя, 25\n"
            "*-  Humanitario*\n\t\t\t📍Ул. Ленина, 51\n"
            "*-  Física y Tecnología*\n\t\t\t📍Ул. Мира, 21\n"
            "*-  Tecnología Química*\n\t\t\t📍ул. Мира, 28\n", parse_mode="Markdown")
        tracked_messages.append(msg.message_id)
        show_main_menu_button(chat_id)

    elif call.data == "back":
        bot.answer_callback_query(call.id, "Regresando al menú principal...")
        clear_secondary_messages(chat_id)  # Eliminar todos los mensajes secundarios
        show_main_menu(chat_id)

# Función para eliminar un mensaje específico
def remove_message(chat_id, message_id):
    try:
        bot.delete_message(chat_id, message_id)
    except Exception as e:
        print(f"Error al eliminar el mensaje: {e}")

# Función para eliminar todos los mensajes secundarios
def clear_secondary_messages(chat_id):
    global tracked_messages
    for message_id in tracked_messages:
        remove_message(chat_id, message_id)
    tracked_messages = []  # Limpiar la lista después de eliminar

# Función para mostrar opciones sobre visas
def show_visa_options(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Primera Visa", callback_data="primera_visa"))
    markup.add(InlineKeyboardButton("🔄 Prolongación de Visa", callback_data="prolongacion_visa"))
    markup.add(InlineKeyboardButton("📜 Registración", callback_data="registracion"))
    markup.add(InlineKeyboardButton("🏫 Tarjeta verde", callback_data="tarjeta-verde"))
    markup.add(InlineKeyboardButton("🔙 Volver al menú principal", callback_data="back"))
    msg = bot.send_message(chat_id, "Selecciona una opción sobre visado:", reply_markup=markup)
    tracked_messages.append(msg.message_id)

def show_direcciones_options(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🏫 Institutos", callback_data="institutos"))
    markup.add(InlineKeyboardButton("🛏️ Dormitorios", callback_data="dormitorios"))
    markup.add(InlineKeyboardButton("🔙 Volver al menú principal", callback_data="back"))
    msg = bot.send_message(chat_id, "Selecciona una opción sobre Direcciones:", reply_markup=markup)
    tracked_messages.append(msg.message_id)

def show_donations_options(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("💳 Donar ahora", url="https://www.tinkoff.ru/rm/molina_barriga.dzheremmi_aleksander1/D8Lkv97917"))
    markup.add(InlineKeyboardButton("🔙 Volver al menú principal", callback_data="back"))
    msg = bot.send_message(chat_id,
                           "El saldo es de *0 ₽* \n¡Gracias por tu interés en apoyar!", reply_markup=markup)
    tracked_messages.append(msg.message_id)


#residencias 
def show_dormitory_options(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🏢 Dormitorio 1️⃣ ", callback_data="dorm1"))
    markup.add(InlineKeyboardButton("🏢 Dormitorio 2️⃣ ", callback_data="dorm2"))
    markup.add(InlineKeyboardButton("🏢 Dormitorio 5️⃣ ", callback_data="dorm5"))
    markup.add(InlineKeyboardButton("🏢 Dormitorio 7️⃣ ", callback_data="dorm7"))
    markup.add(InlineKeyboardButton("🏢 Dormitorio 8️⃣ ", callback_data="dorm8"))
    markup.add(InlineKeyboardButton("🏢 Dormitorio 1️⃣5️⃣ ", callback_data="dorm15"))
    markup.add(InlineKeyboardButton("🏢 Dormitorio 🅽🆅🅺1️⃣ ", callback_data="nvk1"))
    markup.add(InlineKeyboardButton("🏢 Dormitorio 🅽🆅🅺2️⃣ ", callback_data="nvk2"))
    markup.add(InlineKeyboardButton("🔙 Volver al menú principal", callback_data="back"))
    msg = bot.send_message(chat_id, "Selecciona un Dormitorio", reply_markup=markup)
    tracked_messages.append(msg.message_id)

# Botón para regresar al menú principal
def show_main_menu_button(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 Volver al menú principal", callback_data="back"))
    msg = bot.send_message(chat_id, "Selecciona una opción:", reply_markup=markup)
    tracked_messages.append(msg.message_id)

bot.infinity_polling()
