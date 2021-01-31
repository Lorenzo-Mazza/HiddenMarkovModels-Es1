def matrix_fill(list_1d):
    row, column = int(list_1d[0]), int(list_1d[1])
    matrix = [[0.0 for x in range(column)] for y in range(row)]
    counter = 2
    for row_counter in range(row):
        for column_counter in range(column):
            matrix[row_counter][column_counter] = list_1d[counter]
            counter += 1
    return matrix


def computeAlpha():
    for t in range(T):
        for i in range(Nstates):
            if t==0:
                alpha[t][i]= emissions_matrix[i][obs_sequence[t+1]]*init_prob[i+2]
            else:
                sigma = 0
                for j in range(Nstates):
                    sigma += state_trans_matrix[j][i]*alpha[t-1][j]
                alpha[t][i]= emissions_matrix[i][obs_sequence[t+1]]*sigma



inp = input().strip().split(" ")
state_list = list(map(float, inp))
Nstates = int(state_list[0])
state_trans_matrix = matrix_fill(state_list)
inp = input().strip().split(" ")
emissions_list = list(map(float, inp))
emissions_matrix = matrix_fill(emissions_list)
inp = input().strip().split(" ")
init_prob = list(map(float, inp))
inp = input().strip().split(" ")
obs_sequence = list(map(int, inp))
T = obs_sequence[0]
alpha = [[0.0 for j in range(Nstates)] for i in range(T)]
computeAlpha()
obs_seq_probability = 0
for index in range(Nstates):
    obs_seq_probability += alpha[T-1][index]
print(obs_seq_probability)

