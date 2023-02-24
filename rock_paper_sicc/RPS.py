# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
steps = {}
def player(prev_play, opponent_history=[]):
  if prev_play != "":
    opponent_history.append(prev_play)
    
  opp_hist = opponent_history               #Guardamos el historial del oponente
  n = 3                                     #Cantidad de elementos "atras" que observamos
  guess = "R"
  if len(opp_hist) > n:                     #Cuando se supera la cantidad de 
                                            #jugadas guardadas
        pattern = join(opp_hist[-n:])       #Guardamos juntas las ultimas n jugadas como: RPRSP... (n=5)

        if join(opp_hist[-(n + 1):]) in steps.keys(): 
            steps[join(opp_hist[-(n + 1):])] += 1
        else:
            steps[join(opp_hist[-(n + 1):])] = 1

        possible = [pattern + "R", pattern + "P", pattern + "S"]

        for i in possible:
            if not i in steps.keys():
                steps[i] = 0

        predict = max(possible, key=lambda key: steps[key]) # lambda 'argument' : 'function'
                                  # Busca en possible cual de esas combinaciones posee el valor
                                  # mas alto en el diccionario steps 

        if predict[-1] == "P":
            guess = "S"
        if predict[-1] == "R":
            guess = "P"
        if predict[-1] == "S":
            guess = "R"
  return guess

def join(moves):            #Funcion similar a join pero no usa simbolos por lo que si
                            # tenemos [1,2,3] join hara 1""2""3"" osea 123 todo junto
    return "".join(moves)

