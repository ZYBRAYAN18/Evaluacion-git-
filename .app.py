def analisar (lista):
              suma=sum(lista)
              mayor=max(lista)
              menor = min(lista)
              promedio=sum(lista)/len(lista)
              return {
                  "suma": suma,
                  "mayor": mayor,
                  "menor":menor,
                   "promedio":promedio,
              
              }
if __name__==__name__:
  numeros = [4,8,2,10]
  resultado= analisar (numeros) 
  

print (resultado)



         
            