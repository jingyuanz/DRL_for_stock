class Config:
    def __init__(self):
        self.batch_size = 256
        self.hist_length = 400
        self.T = 17
        self.feature_size = 17
        self.gamma = 0.1
        self.MAX_ROUNDS = 1000
        self.init_fund = 10000
        # self.actions = [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.825, 1.0]
        self.actions = [0.0, 1.0]
        self.lstm_dim = 300
        self.n_filter = 300
        self.filter_sizes = [2, 3, 5]
        self.MIN_POOL_SIZE = 5*self.batch_size
        self.dropout = 0.3
        self.lr = 3e-4
        self.epochs = 30
        self.l2_rate = 1e-3
        self.regression_model_path = './model/regressor.json'
        self.regression_weight_path = './model/regressor.h5'
        self.q_json = './model/q.json'
        self.q_weights = './model/q.h5'
        self.result_path = 'data/results.txt'
        self.final_round_model_path = 'model/final.model'
        self.val_best_model_path = 'model/val.model'
        self.predict_model_path = 'model/2018-09-03_best.model'
        self.train_data_path = 'data/train.data'
        self.test_data_path = 'data/test.data'
        self.greediness = 0.008
        self.start_date = '2013-01-01'
        self.chosen_stocks = ['sz50']
        self.prediction_code = 'sz'
        self.MAX_POOL_SIZE = 5000
        self.epsilon = 0.9
        self.cost = 0.15
        self.decay = 0.999
        self.action_size = len(self.actions)
        self.duel_json = './model/duel.json'
        self.duel_weights = './model/duel.h5'