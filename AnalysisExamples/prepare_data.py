


if __name__=="__main__":
    # formats the competitionData into tfRecords for RNN training, including blockwise feature normalization
    baseDir = '/vol/bulkdata/wrb15144/competitionLogData/'

    import os

    os.makedirs(baseDir + '/derived/tfRecords', exist_ok=True)

    from makeTFRecordsFromSession import makeTFRecordsFromCompetitionFiles
    from getSpeechSessionBlocks import getSpeechSessionBlocks

    blockLists = getSpeechSessionBlocks()

    for sessIdx in range(len(blockLists)):
        sessionName = blockLists[sessIdx][0]
        dataPath = "/vol/bulkdata/wrb15144/decoder_data/competitionData/"
        tfRecordFolder = baseDir + '/derived/tfRecords/' + sessionName
        makeTFRecordsFromCompetitionFiles(sessionName, dataPath, tfRecordFolder)
