import pickle
import os

class SaveFile():
    def __init__(self, file_name, data):
        self.file_name=file_name+".pkl"
        if not os.path.exists(self.file_name):
            with open(self.file_name, "wb") as f:
                pickle.dump(data, f)
        else:
            self.save_data(data)

    def read_data(self, keys):
        datas = {}
        if os.path.exists(self.file_name):
            with open(self.file_name, "rb") as f:
                file_datas = pickle.load(f)
            for key in keys:
                datas[key] = file_datas.get(key, {})
            return datas
        else:
            return {"error":"file doesn't exist"}

    def save_data(self, new_datas):
        if os.path.exists(self.file_name):
            with open(self.file_name, "rb") as f:
                datas = pickle.load(f)
            for key in new_datas.keys():
                datas[key] = new_datas[key]
            with open(self.file_name, "wb") as f:
                pickle.dump(datas, f)
            return True
        return False

    def delete_data(self, del_datas):
        if os.path.exists(self.file_name):
            with open(self.file_name, "rb") as f:
                datas = pickle.load(f)
            for key in del_datas.keys():
                datas.pop(key, None)
            with open(self.file_name, "wb") as f:
                pickle.dump(datas, f)
            return True
        return False

    def delete_file(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        self.__del__()

    def __del__(self):
        print(f"close {self.file_name} file")
