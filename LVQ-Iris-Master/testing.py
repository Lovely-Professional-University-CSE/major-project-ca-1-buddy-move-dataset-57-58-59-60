def test_data(wt,data):
    comparison_mat = []
    cl_A = 0
    cl_B = 0
    cl_C = 0
    for q in range(len(data)):
        for g in range(len(wt)):
            for w in range(len(wt[g]) - 1):
                cl_A += (data[q][w] - wt[0][w])
                cl_B += (data[q][w] - wt[1][w])
                cl_C += (data[q][w] - wt[2][w])
                w += 1
            g += 1
        plant_class = data[q][4]
        xw1 = mt.sqrt(cl_A ** 2)
        xw2 = mt.sqrt(cl_B ** 2)
        xw3 = mt.sqrt(cl_C ** 2)
        res = np.array([xw1, xw2, xw3])
        val = np.amin(res)
        if(val == xw1):
            tanaman_type = "IRIS SETOSA"
            winner = wt[0]
        elif (val == xw2):
            tanaman_type = "IRIS VESICOLOR"
            winner = wt[1]
        elif (val == xw3):
            tanaman_type = "IRIS VIRGINICA"
            winner = wt[2]
        print("Plant Type " + str(q + 1)+" = "+tanaman_type+".")
        result = [plant_class,winner[4]]
        comparison_mat.append(result)
        q++1
    right=0
    wrong=0
    for x in range(len(comparison_mat)):
            if(comparison_mat[x][0]==comparison_mat[x][1]):
                right+=1
            else:
                wrong+=1
   def test_data(wt,data):
    comparison_mat = []
    cl_A = 0
    cl_B = 0
    cl_C = 0
    for q in range(len(data)):
        for g in range(len(wt)):
            for w in range(len(wt[g]) - 1):
                cl_A += (data[q][w] - wt[0][w])
                cl_B += (data[q][w] - wt[1][w])
                cl_C += (data[q][w] - wt[2][w])
                w += 1
            g += 1
        plant_class = data[q][4]
        xw1 = mt.sqrt(cl_A ** 2)
        xw2 = mt.sqrt(cl_B ** 2)
        xw3 = mt.sqrt(cl_C ** 2)
        res = np.array([xw1, xw2, xw3])
        val = np.amin(res)
        if(val == xw1):
            tanaman_type = "IRIS SETOSA"
            winner = wt[0]
        elif (val == xw2):
            tanaman_type = "IRIS VESICOLOR"
            winner = wt[1]
        elif (val == xw3):
            tanaman_type = "IRIS VIRGINICA"
            winner = wt[2]
        print("Plant Type " + str(q + 1)+" = "+tanaman_type+".")
        result = [plant_class,winner[4]]
        comparison_mat.append(result)
        q++1
    right=0
    wrong=0
    for x in range(len(comparison_mat)):
            if(comparison_mat[x][0]==comparison_mat[x][1]):
                right+=1
            else:
                wrong+=1
    print("Models Accuracy = "+ str((float(right)/(right+wrong))*100) +"%")
