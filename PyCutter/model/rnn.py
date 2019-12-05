import torch.nn as nn


class BiLSTM(nn.Module):

    def __init__(self, vocab_size, embed_dim=300, hidden_dim=256):
        """ 双向LSTM分词模型

        Args:
            vocab_szie: 字的个数
            embed_dim: 嵌入维度
            hidden_dim: 隐藏层大小
        """
        self.embedder = nn.Embedding(vocab_size, embed_dim)
        self.rnn = nn.LSTM(embed_dim, hidden_dim, bidirectional=True)


    def forward(self):
        pass
