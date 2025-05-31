from multiprocessing import Process

def DataProcessing(word):    #   :)
    with open(f'file11.txt', 'a') as f:
        f.writelines(str(word))

if __name__ == '__main__':
    p1 = Process(target=DataProcessing, args=('simvol2 ',), daemon=True)
    p2 = Process(target=DataProcessing, args=('simvol1 ',), daemon=True)
    p1.start()
    p2.start()
    p1.join()
    p2.join()