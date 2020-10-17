import os
import glob
import importlib

class Transliterate:
	def __init__(self, text, language_input = None, language_output = None):
		self.text = text.lower()
		if language_output is None:
			raise ValueError("Укажите выходной язык")
		elif language_input is None:
			raise ValueError("Укажите язык оригинала")
		else:
			if language_output.isalpha() and language_input.isalpha():
				if len(language_output) == 2 and len(language_input) == 2: 
					for i in glob.glob("./language/*"):
						if i[-2:] == language_output:
							self.language_output = language_output.lower()
							break
					else:
						raise ValueError("Укажите верный выходящий язык")

					for i in glob.glob("./language/*"):
						if i[-2:] == language_input:
							self.language_input = language_input
							break
					else:
						raise ValueError("Укажите верный язык оригинала")
				else:
					raise ValueError("Длина языка не может привышать 2 символа")
			else:
				raise ValueError("Название языков не может быть с числом")

	def translite(self):
		for i in glob.glob(f".\\language\\{self.language_input}\\{self.language_input}-{self.language_output}"):
			for l in glob.glob(i + "\\*"):
				if os.path.basename(l).endswith(".py") and os.path.basename(l).startswith("litters"):
					file = importlib.import_module(l.replace("\\", ".")[2:-3])

		for key in file.litters:
			self.text = self.text.replace(key, file.litters[key])

		return self.text

iam = Transliterate("privet", language_input = "en", language_output = "ru")
iam.translite()