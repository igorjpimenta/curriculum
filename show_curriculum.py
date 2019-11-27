from chart_library import pie_chart, scatter_plot
from IPython.display import display, HTML

def show(info, resume, exp, edu, comp, lang):
    display(HTML('<center><h1>' + info['fullname'] + '</h1></center>'))
    display(HTML('<center><big>' + info['nationality'] + ', ' + info['age'] + '</big></center>'))
    display(HTML('<center><big>' + info['address'] + '</big></center>'))
    display(HTML('<center><big> Contatos: ' + info['contact']['cellphone'] + ' | <a>' + info['contact']['email'] + '</a></big></center>'))
    display(HTML('<center><big> Linkedin: <a>' + info['social']['linkedin'] + '</a></big></center>'))
    display(HTML('<center><big> Github: <a>' + info['social']['github'] + '</a></big></center>'))
    display(HTML('<h2> Resumo </h2>'))
    display(HTML('<big>' + resume + '</big>'))
    display(HTML('<h2> Experiência </h2>'))
    display(HTML('<h3>' + exp['current']['company'] + '</h3>'))
    display(HTML('<big><b> • ' + exp['current']['function'] + ' | ' + exp['current']['time'] + '</b></big>'))
    display(HTML('<big>' + exp['current']['assignments'] + '</big>'))
    display(HTML('<big><b> • ' + exp['last']['function'] + ' | ' + exp['last']['time'] + '</b></big>'))
    display(HTML('<big>' + exp['last']['assignments'] + '</big>'))
    
    scatter_plot(comp, 'Ferramentas e habilidades', [['Prática', 'Conhecimento'], ['Utilização', 'Aprendizado']])
    
    display(HTML('<h2> Formação </h2>'))
    display(HTML('<big>' + edu['course'] + '</big>'))
    display(HTML('<big>' + edu['school'] + '</big>'))
    display(HTML('<big>' + edu['time'] + '</big>'))

    pie_chart({k: v for k, v in lang.items() if k != 'language'}, 'Proeficiência em inglês')