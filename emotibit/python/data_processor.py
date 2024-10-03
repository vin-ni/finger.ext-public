import neurokit2 as nk

def process_eda(eda_signal):
    # print(eda_signal)
    # Clean EDA signal
    eda_cleaned = nk.eda_clean(eda_signal, sampling_rate=15)
    eda = nk.eda_phasic(eda_cleaned, sampling_rate=15)
    eda_phasic = eda["EDA_Phasic"].values
    # print(cleaned_eda)
    # Decompose into phasic and tonic components
    # highpass = nk.eda_phasic(cleaned_eda, sampling_rate=15, method='highpass')
    
    # eda_signal = nk.eda_simulate(duration=2, scr_number=5, noise=0, sampling_rate=15)
    # signals, info = nk.eda_process(eda_signal, sampling_rate=15)

    # https://neuropsychology.github.io/NeuroKit/functions/eda.html
    # signals = nk.eda_process(eda_signal, sampling_rate=15)
    
    return eda_cleaned, eda_phasic