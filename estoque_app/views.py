from django.shortcuts import render, redirect
from .models import Estoque
from datetime import date as dt
from datetime import datetime, timedelta
import os 
import smtplib
from email.message import EmailMessage

#import datetime as dt


# Create your views here.
def home(request):
        
        EMAIL_ANDRESS = ""
        EMAIL_SENHA = ""


        msg = EmailMessage()
        msg['Subject'] = "Tema do Email"
        msg['From'] = "seuemail"
        msg['To'] = "emaildapessoa"
        msg.set_content('Mensagem do email')


        '''
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
             smtp.login(EMAIL_ANDRESS,EMAIL_SENHA)
             smtp.send_message(msg)
        
        
        '''
        
        
        
        data = dt.today()
        dia = data.day
        mes = data.month
        ano = data.year

     
        print(data.day)

        hoje = '{}/{}/{}'.format(dia,mes,ano)
        
        #O problema está em reconhecimento de datas no formato q queremos portanto resolvendo isso tá de boas
        
        print("olha aqui ",data + timedelta(days=1))

        #print(dt('2023-08-30'))

        situacao = []

        for i in Estoque.objects.all():
             validad = dt(i.validade.year,i.validade.month,i.validade.day) - data;
             print("teste => ",validad.days)

             if(int(validad.days) < 0):
                    situacao.append("vencido");
             else:
                    situacao.append("emDia");
                    
             

        print(situacao);

        n = 100;

        resPra = []
        mediaDPessoas = []

        tudo = []

        vencidas = 0;
        nVencidas = 0;
        
        for i in Estoque.objects.all():
                print(i.quantidade_qtd)
                qtd = i.quantidade_qtd
                porcao = i.porcao
                novaq = (porcao * n)/1000; 
                resPra.append(novaq)

                validad = dt(i.validade.year,i.validade.month,i.validade.day) - data;

               
                novaValidade = '{}/{}/{}'.format(i.validade.day,i.validade.month,i.validade.year)
                #print("teste => ",validad.days)

                if(int(validad.days) < 0):
                        tudo.append({
                        "id_uni": i.id_uni,
                        "alimento":i.alimento,
                        "quantidade_qtd":i.quantidade_qtd,
                        "validade":novaValidade,
                        "porcao":i.porcao,
                        "prazo":"table-danger"
                        })
                        vencidas =+ 1;
                        #situacao.append("vencido");
                else:
                        pessoa = qtd * 1000 / porcao;
                        mediaDPessoas.append(pessoa)
                        tudo.append({
                        "id_uni": i.id_uni,
                        "alimento":i.alimento,
                        "quantidade_qtd":i.quantidade_qtd,
                        "validade":novaValidade,
                        "porcao":i.porcao,
                        "prazo":"emDia"
                        })
                        nVencidas =+ 1;






        media_de_pessoas = sum(mediaDPessoas)/len(mediaDPessoas)
        qtd_alimentos_na_validade = len(tudo) - vencidas

        estoque = { 'es': tudo, 'hora': hoje,
                    "prazo": situacao,
                    "mediaPessoas":int(media_de_pessoas),
                    "vencidas":vencidas,
                    "nVencidas":qtd_alimentos_na_validade
                      }

        return render(request,'home.html',estoque)


def register(request):

    estoque = Estoque()
    

    if request.method == "POST":

        estoque.alimento = request.POST.get('alimento')
        estoque.quantidade_qtd = request.POST.get('qtd')
        estoque.validade = request.POST.get('validade')
        estoque.porcao = request.POST.get('porcao')

        estoque.save()

        return redirect('home')
    else:
        return render(request,'register.html')



def pratos(request):
       
       n = 100;

       resPra = []
       mediaDPessoas = []
       
       for i in Estoque.objects.all():
              print(i.quantidade_qtd)
              qtd = i.quantidade_qtd
              porcao = i.porcao
              novaq = (porcao * n)/1000; 
              resPra.append(novaq)
              pessoa = qtd * 1000 / porcao;
              mediaDPessoas.append(pessoa)
              porc = (qtd * 1000)/ pessoa;





              

              print("nova qtd ",novaq);
              print("porcao2 ",porc);
              media = sum(resPra) / len(resPra);


              print("pessoas ",pessoa);
       
       media_de_pessoas = sum(mediaDPessoas)/len(mediaDPessoas)

       #calculo por pessoa
       for i in Estoque.objects.filter(quantidade_qtd__gte=media):
              print(i.alimento)
        
        
       pratos = {
               "alimentos": Estoque.objects.filter(quantidade_qtd__gte=media),
               "mediaPessoas":int(media_de_pessoas)
        }

       return render(request,"pratos.html",pratos)
    



''''
         



             

             dom = []
             seg = []
             ter = []
             qua = []
             qui = []
             sex = []
             sab = []
        



             for i in range(0,34):
                    
                    dias = data + timedelta(days=i)
                    if dias.weekday() == 0:
                            seg.append(dias.day)
                    if dias.weekday() == 1:
                            ter.append(dias.day)
                    if dias.weekday() == 2:
                            qua.append(dias.day)
                    if dias.weekday() == 3:
                            qui.append(dias.day)
                    if dias.weekday() == 4:
                            sex.append(dias.day)
                    if dias.weekday() == 5:
                            sab.append(dias.day)
                    if dias.weekday() == 6:
                            dom.append(dias.day)
                        
                    
             dom = []
             seg = []
             ter = []
             qua = []
             qui = []
             sex = []
             sab = []




             for i in range(0,34):
                    
                    dias = data + timedelta(days=i)
                    if dias.weekday() == 0:
                            seg.append(dias.day)
                    if dias.weekday() == 1:
                            ter.append(dias.day)
                    if dias.weekday() == 2:
                            qua.append(dias.day)
                    if dias.weekday() == 3:
                            qui.append(dias.day)
                    if dias.weekday() == 4:
                            sex.append(dias.day)
                    if dias.weekday() == 5:
                            sab.append(dias.day)
                    if dias.weekday() == 6:
                            dom.append(dias.day)
                        
                    
                        
                dom = []
                seg = []
                ter = []
                qua = []
                qui = []
                sex = []
                sab = []




                for i in range(0,34):
                    
                    dias = hoje + timedelta(days=i)
                    if dias.weekday() == 0:
                            seg.append(dias.day)
                    if dias.weekday() == 1:
                            ter.append(dias.day)
                    if dias.weekday() == 2:
                            qua.append(dias.day)
                    if dias.weekday() == 3:
                            qui.append(dias.day)
                    if dias.weekday() == 4:
                            sex.append(dias.day)
                    if dias.weekday() == 5:
                            sab.append(dias.day)
                    if dias.weekday() == 6:
                            dom.append(dias.day)
                        
                    
                    #dias = hoje + timedelta(days=i)
                        
                    print(dias)
                    


                    


                    #print(dias.day,"/",dias.month,"/",dias.year,"- ",dias.weekday())



                print(dom)

                semanas = {
                    "dom":dom,
                    "seg":seg,
                    "ter":ter,
                    "qua":qua,
                    "qui":qui,
                    "sex":sex,
                    "sab":sab
                }
'''