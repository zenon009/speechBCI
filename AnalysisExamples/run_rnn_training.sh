python3 -m neuralDecoder.main \
    dataset=speech_release_baseline \
    model=gru_stack_inputNet \
    learnRateDecaySteps=10000 \
    nBatchesToTrain=10000  \
    learnRateStart=0.02 \
    model.nUnits=1024 \
    model.stack_kwargs.kernel_size=32 \
    outputDir=/home/wrb15144/speechPaperRelease_08_20//derived/rnns/baselineRelease