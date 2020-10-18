import os
import glob
import importlib

class Transliterate:
	def __init__(self, text, language_input = None, language_output = None):
		self.text = text
		if language_output is None:
			raise ValueError("Укажите выходной язык")
		if language_input is None:
			raise ValueError("Укажите язык оригинала")
		if language_output.lower().isalpha() and language_input.lower().isalpha():
			if len(language_output) == 2 and len(language_input) == 2:
				if language_output.lower() == language_input.lower():
					raise ValueError("Выходной и оригинальный язык не могут быть одинаковыми")
				else:
					for i in glob.glob("./language/*"):
						if i[-2:] == language_output.lower():
							self.language_output = language_output.lower()
							break
					else:
						raise ValueError("Укажите верный выходящий язык")

					for i in glob.glob("./language/*"):
						if i[-2:] == language_input.lower():
							self.language_input = language_input.lower()
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

		if file.__hieroglyphs__:
			self.text = self.text.lower()
			for key in file.litters:
				self.text = self.text.replace(key, file.litters[key])
		else:
			for key in file.litters:
				self.text = self.text.replace(key, file.litters[key])
	
		return self.text

iam = Transliterate("rривет", language_output = "en")
print(iam.translite())