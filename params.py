import os

class Parameters():
    def __init__(self):
        self.n_processors = 8
        # Path\
        self.data_dir =  'C:\\Users\\vilad\\OneDrive - campus.udg.edu\\Documents [UdG-GEINF]\\2022-2023\\Tècniques Avançades d\'Intel·ligència Artifcial [P.Inf]\\Projecte\\dataset\\dataset\\'
        self.image_dir = self.data_dir + 'sequences\\'
        self.pose_dir = self.data_dir + 'poses\\'

        self.train_video = ['00', '01', '02', '05', '08', '09']
        self.valid_video = ['04', '06', '07', '10']
        self.partition = None  # partition videos in 'train_video' to train / valid dataset  #0.8


        # Data Preprocessing
        self.resize_mode = 'rescale'  # choice: 'crop' 'rescale' None
        self.img_w = 608   # original size is about 1226
        self.img_h = 184   # original size is about 370
        self.img_means = -0.1389521052731338
        self.img_means_np = 92.0672126539245
        self.img_stds = 0.2911982605213023
        self.img_stds_np = 74.25555314703192
        self.minus_point_5 = True

        self.seq_len = (5, 7)
        self.sample_times = 1

        # Data info path
        self.train_data_info_path = 'datainfo/train_df_t{}_v{}_p{}_seq{}x{}_sample{}.pickle'.format(''.join(self.train_video), ''.join(self.valid_video), self.partition, self.seq_len[0], self.seq_len[1], self.sample_times)
        self.valid_data_info_path = 'datainfo/valid_df_t{}_v{}_p{}_seq{}x{}_sample{}.pickle'.format(''.join(self.train_video), ''.join(self.valid_video), self.partition, self.seq_len[0], self.seq_len[1], self.sample_times)


        # Model
        self.rnn_hidden_size = 448
        self.conv_dropout = (0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.5)
        self.rnn_dropout_out = 0.5
        self.rnn_dropout_between = 0   # 0: no dropout
        self.clip = None
        self.batch_norm = True
        # Training
        self.epochs = 250
        self.batch_size = 8
        self.pin_mem = True
        self.optim = {'opt': 'Adagrad', 'lr': 0.0005}
                    # Choice:
                    # {'opt': 'Adagrad', 'lr': 0.001}
                    # {'opt': 'Adam'}
                    # {'opt': 'Cosine', 'T': 100 , 'lr': 0.001}

        # Pretrain, Resume training
        self.pretrained_flownet = None
                                # Choice:
                                # None
                                # './pretrained/flownets_bn_EPE2.459.pth.tar'  
                                # './pretrained/flownets_EPE1.951.pth.tar'
        self.resume = False  # resume training
        self.resume_t_or_v = '.train'
        self.load_model_path = 'models/t{}_v{}_im{}x{}_s{}x{}_b{}_rnn{}_{}.model{}'.format(''.join(self.train_video), ''.join(self.valid_video), self.img_h, self.img_w, self.seq_len[0], self.seq_len[1], self.batch_size, self.rnn_hidden_size, '_'.join([k+str(v) for k, v in self.optim.items()]), self.resume_t_or_v)
        self.load_optimizer_path = 'models/t{}_v{}_im{}x{}_s{}x{}_b{}_rnn{}_{}.optimizer{}'.format(''.join(self.train_video), ''.join(self.valid_video), self.img_h, self.img_w, self.seq_len[0], self.seq_len[1], self.batch_size, self.rnn_hidden_size, '_'.join([k+str(v) for k, v in self.optim.items()]), self.resume_t_or_v)

        self.record_path = 'records/t{}_v{}_im{}x{}_s{}x{}_b{}_rnn{}_{}.txt'.format(''.join(self.train_video), ''.join(self.valid_video), self.img_h, self.img_w, self.seq_len[0], self.seq_len[1], self.batch_size, self.rnn_hidden_size, '_'.join([k+str(v) for k, v in self.optim.items()]))
        self.save_model_path = 'models/t{}_v{}_im{}x{}_s{}x{}_b{}_rnn{}_{}.model'.format(''.join(self.train_video), ''.join(self.valid_video), self.img_h, self.img_w, self.seq_len[0], self.seq_len[1], self.batch_size, self.rnn_hidden_size, '_'.join([k+str(v) for k, v in self.optim.items()]))
        self.save_optimzer_path = 'models/t{}_v{}_im{}x{}_s{}x{}_b{}_rnn{}_{}.optimizer'.format(''.join(self.train_video), ''.join(self.valid_video), self.img_h, self.img_w, self.seq_len[0], self.seq_len[1], self.batch_size, self.rnn_hidden_size, '_'.join([k+str(v) for k, v in self.optim.items()]))


        if not os.path.isdir(os.path.dirname(self.record_path)):
            os.makedirs(os.path.dirname(self.record_path))
        if not os.path.isdir(os.path.dirname(self.save_model_path)):
            os.makedirs(os.path.dirname(self.save_model_path))
        if not os.path.isdir(os.path.dirname(self.save_optimzer_path)):
            os.makedirs(os.path.dirname(self.save_optimzer_path))
        if not os.path.isdir(os.path.dirname(self.train_data_info_path)):
            os.makedirs(os.path.dirname(self.train_data_info_path))

par = Parameters()

