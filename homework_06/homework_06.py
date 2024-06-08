from pywebio.input import textarea
from pywebio.output import put_text, put_image, put_html

import messages

# configuration
main_image_path = 'homework_06/surfing.jpg.webp'

# presentation
put_html(f'<h1>{messages.PAGE_HEADER}</h1>')
put_text(messages.PAGE_CONTENT)

user_summer_agenda = textarea(messages.SUMMER_AGENDA_REQUEST, rows=5, placeholder=messages.SUMMER_AGENDA_REQUEST)
put_text(messages.SUMMER_AGENDA_INFO.format(
  length=len(user_summer_agenda)
))

main_img = open(main_image_path, 'rb').read()
put_image(main_img, width='500px')
