"""
Configuration for the google speech commands task
"""

# TODO: move some of these to a global config and import that here
# See: https://github.com/neuralaudio/hear2021-eval-kit/issues/10

TASKNAME = "speech_commands-v0.0.2"
DOWNLOAD_URL = "http://download.tensorflow.org/data/speech_commands_v0.02.tar.gz"
TEST_DOWNLOAD_URL = (
    "http://download.tensorflow.org/data/speech_commands_test_set_v0.02.tar.gz"
)
SEED = 43

# Number of CPU workers for Luigi jobs
NUM_WORKERS = 4

# If you only use one sample rate, you should have an array with
# one sample rate in it.
# However, if you are evaluating multiple embeddings, you might
# want them all.
SAMPLE_RATES = [48000, 44100, 22050, 16000]

SAMPLE_LENGTH_SECONDS = 1.0

# TODO: Do we want to call this FRAME_RATE or HOP_SIZE
FRAME_RATE = 4

# Set this to None if you want to use ALL the data.
# NOTE: This will be, expected, 225 test files only :\
# NOTE: You can make this smaller during development of this
# preprocessing script, to keep the pipeline fast.
# WARNING: If you change this value, you *must* delete _workdir
# or working dir.
# Most of the tasks iterate over every audio file present,
# except for the one that downsamples the corpus.
# (This is why we should have one working directory per task)
MAX_FRAMES_PER_CORPUS = 20 * 3600

MAX_FILES_PER_CORPUS = 1000
