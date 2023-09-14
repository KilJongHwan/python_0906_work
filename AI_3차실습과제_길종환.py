from sklearn.neural_network import MLPClassifier

# 훈련 집합 구축 

X=[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]] 

y=[-1,1,-1,-1,-1,-1,1,-1] 


# fit 함수로 Perceptron 학습 

#[3-4.아래 실행결과가 나오도록 코드 작성] 

mlp = MLPClassifier(hidden_layer_sizes=(100), learning_rate_init=0.001, batch_size=32 ,max_iter=300, solver='sgd', verbose= True )
mlp.fit(X, y)


#print("학습된 퍼셉트론의 매개변수: ",p.coef_,p.intercept_) 

print("학습된 퍼셉트론의 매개변수(가중치):\n",mlp.coefs_,"\n",mlp.intercepts_) 

print("훈련집합에 대한 예측: ",mlp.predict(X)) 

print("정확률 측정: ",mlp.score(X,y)*100,"%") 