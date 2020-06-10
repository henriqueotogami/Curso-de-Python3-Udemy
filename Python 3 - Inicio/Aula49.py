{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#Instalação dos módulos Anaconda: Scipy, numpy, sklearn, ipython e Jupiter notebook"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#Iris Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "output_type": "error",
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'sklearn'",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-808b7766c59e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdatasets\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mload_iris\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0miris\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mload_iris\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0miris\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'sklearn'"
     ]
    }
   ],
   "source": [
    "from sklearn.datasets import load_iris\n",
    "iris = load_iris()\n",
    "print(iris)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.1-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python38132bitc5421e651e99468086e94c74e56f53cd",
   "display_name": "Python 3.8.1 32-bit"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}