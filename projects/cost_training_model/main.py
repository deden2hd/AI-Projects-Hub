# Estimasi Total Biaya Training Model AI

def cost_training_model(num_gpu, cost_per_gpu_hour, hours_per_day, days_training):
    '''
    Skenario:
    Kamu bekerja sebagai AI Engineer di sebuah perusahaan AI besar (misalnya DeepSeek, OpenAI, atau Gemini).
    Tugas kamu adalah menghitung total biaya training model AI yang akan dijalankan pada sebuah cluster GPU.
    Informasi yang diberikan adalah.

    parameters:
    num_gpu (int) : Jumlah GPU.
    cost_per_gpu_hour (float) : Biaya running GPU per jamnya.
    hours_per_day : Berapa jam GPU akan diaktifkan untuk 1 hari.
    days_training : Jumlah hari GPU diaktifkan

    example:
    >>> cost_training_model(8, 2.50, 8, 7)     
    Total jam training: 56
    Biaya training per GPU: 140.0
    Total biaya training untuk 8 GPU: 1120.0

    return: 56, 140.0, 1120.0
    '''

    # Hitung Total Jam Training:
    total_hours = hours_per_day * days_training

    # Hitung Total Biaya per GPU:
    cost_per_gpu = cost_per_gpu_hour * total_hours

    # Hitung Total Biaya Training:
    total_cost = cost_per_gpu * num_gpu

    print(f"Total jam training: {total_hours}")
    print(f"Biaya training per GPU: {cost_per_gpu}")
    print(f"Total biaya training untuk {num_gpu} GPU: {total_cost}")

    return total_hours, cost_per_gpu, total_cost

if __name__ == "__main__":

    # Deklarasi Variable
    num_gpu = int(input("Jumlah GPU yang digunakan: "))
    cost_per_gpu_hour = float(input("Biaya per GPU per jam: "))
    hours_per_day = int(input("Jumlah jam training per hari: "))
    days_training = int(input("Jumlah hari training: "))

    #  Menjalankan program menghitung biaya
    cost_training_model(num_gpu, cost_per_gpu_hour, hours_per_day, days_training)
