from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'project2'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fdfxmirf:i2yUyPRIytvSLC2DAUUm35C8KhTr838l@kesavan.db.elephantsql.com/fdfxmirf'
db = SQLAlchemy(app)

class Portifolio(db.Model):
   id = db.Column(db.Integer, primary_key = True, autoincrement=True )
   nome = db.Column(db.String(150), nullable=False)
   imagem = db.Column(db.String(500), nullable=False)
   descricao = db.Column(db.String(500), nullable=False)
   video = db.Column(db.String(500), nullable=False)
   autor = db.Column(db.String(150), nullable=False)

   def __init__(self, nome, imagem, descricao, video, autor):
      self.nome = nome
      self.imagem = imagem
      self.descricao = descricao
      self.video = video
      self.autor = autor



### Criando rotas abaixo###
@app.route('/') # renderiza a pagina principal(rota)
def index():
    
    return render_template('index.html')

@app.route('/adm')
def adm():
   portifolio = Portifolio.query.all() #vai ler tudo, select * from projetos
   return render_template('adm.html', portifolio=portifolio)
### create#####
@app.route('/new', methods=['GET', 'POST'])
def new(): # new definido no formulario de inclusao na pagina adm
   if request.method == 'POST': # Verifica se o metodo recebido na requisição é POST
      # cria o objeto projeto, adiconando os campos do form nele.
      portifolio = Portifolio(
         request.form['nome'],
         request.form['imagem'],
         request.form['descricao'],
         request.form['video'],
         request.form['autor']
      )
      db.session.add(portifolio) # Adiciona o objeto projeto no banco de dados.
      db.session.commit() # Confirma a operação
      flash('Confia, deu bom')
      return redirect('/adm') 



#######
@app.route('/antonio') # renderiza a pagina principal(rota)
def antonio():
    # portifolio = Portifolio.query.all()
    portifolio = Portifolio.query.filter_by(autor='ANTONIO') #faz o filtro
   
    return render_template('antonio.html', portifolio=portifolio )

@app.route('/elisama') # renderiza a pagina principal(rota)
def elisama():
    # projetos = Projeto.query.all()
    return render_template('elisama.html')

@app.route('/fellipe') # renderiza a pagina principal(rota)
def fellipe():
    # projetos = Projeto.query.all()
    return render_template('fellipe.html')

@app.route('/marcelo') # renderiza a pagina principal(rota)
def marcelo():
    # projetos = Projeto.query.all()
    return render_template('marcelo.html')

@app.route('/rudhy') # renderiza a pagina principal(rota)
def rudhy():
    # projetos = Projeto.query.all()
    return render_template('rudhy.html')



if __name__ == '__main__':
   db.create_all() #cria o banco de dados 
   app.run(debug=True)