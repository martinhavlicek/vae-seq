"""Hyperparameters used in this library."""

import tensorflow as tf

_DEFAULTS = dict(
    # Number of latent units per time step
    latent_size=4,

    # Model parameters
    obs_encoder_fc_layers=[256, 128],
    obs_decoder_fc_hidden_layers=[256],
    latent_decoder_fc_layers=[256],
    rnn_hidden_sizes=[32],

    # Default activation (relu/elu/etc.)
    activation='relu',

    # Postivitity constraint (softplus/exp/etc.)
    positive_projection='softplus',

    # VAE params
    divergence_strength_halfway_point=1e4,  # global steps.
    vae_type='SRNN',  # See vae.VAE_TYPES.
    use_monte_carlo_kl=False,
    srnn_use_res_q=True,

    # Training parameters
    batch_size=20,
    sequence_size=5,
    learning_rate=0.0001,
    agent_learning_rate=0.01 * 0.0001,
    clip_gradient_norm=1.,
    check_numerics=True,
    reinforce_agent_across_timesteps=True,
)

def make_hparams(flag_value=None, **kwargs):
    """Initialize HParams with the defaults in this module."""
    init = dict(_DEFAULTS)
    init.update(kwargs)
    ret = tf.contrib.training.HParams(**init)
    if flag_value:
        ret.parse(flag_value)
    return ret