# checkpoints
logs_hyperparams = {'chkp_dir': 'chkp2/',
                    'log_dir': 'logs/train_logs/',
                    'gen_dir': 'generated2/',
                    # None if training from the scratch
                    'chkp_name_gen': 0,
                    'chkp_name_dis': 0
                    }

# check gpu devices
train_mode = {'gpu': True,
              'gpu_devices': '3',
              'multi_gpu': False
}

print_summary = True
model_hyperparams = {'clip_norm': 1e-2,
                     'function': 'gaussian_roi', # roi generation function
                     'spectral_norm': True,
                     'dis_n_features': 64 # n_features in discriminator
}

gen_hyperparams = {'init_size': (8, 8),
                    'dest_size': (64, 64),
                    'scale': 2,
                    'input_channels': 128,
                    'kernel_size': 3
}

noise_hyperparams = {
    'noise_dim': 146,
    'cont_dim': 10,
    'disc_dim': 10,
    'n_disc': 10
}

stabilizing_hyperparams = {'adding_noise': True
}

discriminator_stabilizing_hyperparams = {'fe_matching': True,
                                         #'n_layers_fe_matching': list(range(12)),
                                         'n_layers_fe_matching': [1, 4, 7, 10, 13],
                                         #'wgan_clip_size': 1e-2,
                                         'wgan_clip_size': None,
                                         'loss': 'hinge' # 'ls', 'wgan', 'softplus', 'hinge'
}

generator_stabilizing_hyperparams = {'roi_loss': False,
                                     'vae_loss': True,
                                     'loss': 'hinge' # 'ls', 'wgan', 'softplus', 'hinge'
}

# train/test hyperparameters
train_hyperparams = {'num_epochs': 400,
                    'batch_size': 32,
                    'sample_interval': 500
}

# add lr-scheduling possibility
optimizator_hyperparams = {#'lr_gen': 0.0001,
                           #'lr_dis': 0.0005
                            'lr_gen': 0.0001,
                            'lr_dis': 0.0003
}

# dataset constants
dataset = 'Cats'

datasets_hyperparams = {'CelebA': {#'mean': [0.5061, 0.4254, 0.3828],
                                   # 'std': [0.3043, 0.2838, 0.2833],
                                    'mean': [0.5] * 3,
                                    'std': [0.5] * 3,
                                    'path': 'celeba_train/',
                                    'img_shape': (64, 64)
                                    },
                        'Cats': {#'mean': [0.5061, 0.4254, 0.3828],
                                   # 'std': [0.3043, 0.2838, 0.2833],
                                    'mean': [0.5] * 3,
                                    'std': [0.5] * 3,
                                    'path': 'cats/',
                                    'img_shape': (64, 64)
                                    },
                        'Cars': {#'mean': [0.5061, 0.4254, 0.3828],
                                   # 'std': [0.3043, 0.2838, 0.2833],
                                    'mean': [0.5] * 3,
                                    'std': [0.5] * 3,
                                    'path': 'cars_train/',
                                    'img_shape': (64, 64)
                                    }
                        }
