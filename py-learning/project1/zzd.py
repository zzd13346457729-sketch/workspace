import numpy as np
import pandas as pd
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import warnings

warnings.filterwarnings('ignore')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet', quiet=True)

np.random.seed(42)

print("=" * 60)
print("新闻主题分类分析项目")
print("=" * 60)

print("\n1. 正在加载数据集...")
categories = ['comp.graphics', 'talk.religion.misc', 'sci.space', 'rec.sport.baseball']

news_data = fetch_20newsgroups(
    subset='all',
    categories=categories,
    shuffle=True,
    random_state=42,
    remove=('headers', 'footers', 'quotes')
)

df_news = pd.DataFrame({
    'text': news_data.data,
    'category_id': news_data.target
})

df_news['category'] = df_news['category_id'].apply(
    lambda x: news_data.target_names[x]
)

print(f"数据集加载完成，共 {len(df_news)} 条记录")
print("类别分布统计:")
print(df_news['category'].value_counts())

print("\n2. 正在进行文本预处理...")

stop_words = set(stopwords.words('english'))
word_lemmatizer = WordNetLemmatizer()


def clean_news_text(raw_text):
    if not isinstance(raw_text, str):
        return ""

    cleaned = raw_text.replace('\n', ' ').replace('\t', ' ')
    cleaned = re.sub(r'\S+@\S+\.\S+', '', cleaned)
    cleaned = re.sub(r'http\S+|www\.\S+', '', cleaned)
    cleaned = re.sub(r'[^a-zA-Z\s]', ' ', cleaned)
    cleaned = cleaned.lower()

    words = word_tokenize(cleaned)

    meaningful_words = []
    for word in words:
        if word not in stop_words and len(word) > 2:
            lemma = word_lemmatizer.lemmatize(word)
            meaningful_words.append(lemma)

    return ' '.join(meaningful_words)


df_news['cleaned_text'] = df_news['text'].apply(clean_news_text)

initial_count = len(df_news)
df_news = df_news[df_news['cleaned_text'].str.len() > 10]
print(f"移除了 {initial_count - len(df_news)} 条空文本记录")

print("\n3. 正在提取TF-IDF特征...")

tfidf_extractor = TfidfVectorizer(
    max_features=5000,
    min_df=5,
    max_df=0.8,
    ngram_range=(1, 2)
)

X_features = tfidf_extractor.fit_transform(df_news['cleaned_text'])
y_labels = df_news['category_id']

print(f"特征矩阵形状: {X_features.shape}")

print("\n4. 划分训练集和测试集...")
X_train, X_test, y_train, y_test = train_test_split(
    X_features, y_labels,
    test_size=0.25,
    random_state=42,
    stratify=y_labels
)

print(f"训练集样本数: {X_train.shape[0]}")
print(f"测试集样本数: {X_test.shape[0]}")

print("\n5. 模型训练与评估")
print("-" * 40)

print("\n模型A: 多项式朴素贝叶斯分类器")
nb_model = MultinomialNB(alpha=0.1)
nb_model.fit(X_train, y_train)

y_pred_nb = nb_model.predict(X_test)
nb_accuracy = accuracy_score(y_test, y_pred_nb)

print(f"测试集准确率: {nb_accuracy:.4f}")
print("详细分类报告:")
print(classification_report(y_test, y_pred_nb, target_names=news_data.target_names))

print("\n模型B: 线性支持向量机")
svm_model = LinearSVC(
    C=1.0,
    random_state=42,
    max_iter=2000
)
svm_model.fit(X_train, y_train)

y_pred_svm = svm_model.predict(X_test)
svm_accuracy = accuracy_score(y_test, y_pred_svm)

print(f"测试集准确率: {svm_accuracy:.4f}")
print("详细分类报告:")
print(classification_report(y_test, y_pred_svm, target_names=news_data.target_names))

print("\n6. 5折交叉验证结果")
print("-" * 40)

nb_cv_scores = cross_val_score(
    MultinomialNB(alpha=0.1),
    X_features, y_labels,
    cv=5,
    scoring='accuracy'
)

svm_cv_scores = cross_val_score(
    LinearSVC(C=1.0, random_state=42, max_iter=2000),
    X_features, y_labels,
    cv=5,
    scoring='accuracy'
)

print(f"朴素贝叶斯平均准确率: {nb_cv_scores.mean():.4f} (±{nb_cv_scores.std():.4f})")
print(f"SVM平均准确率: {svm_cv_scores.mean():.4f} (±{svm_cv_scores.std():.4f})")

print("\n7. 生成可视化图表...")

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

fig1, ax1 = plt.subplots(figsize=(10, 6))
category_counts = df_news['category'].value_counts()
bars = ax1.bar(category_counts.index, category_counts.values)
ax1.set_title('新闻数据集类别分布', fontsize=16, fontweight='bold')
ax1.set_xlabel('新闻类别', fontsize=12)
ax1.set_ylabel('文章数量', fontsize=12)

for bar, count in zip(bars, category_counts.values):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2., height + 5,
             f'{count}', ha='center', va='bottom')

plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('category_distribution.png', dpi=300, bbox_inches='tight')
print("已保存: category_distribution.png")

fig2, ax2 = plt.subplots(figsize=(9, 7))
conf_matrix = confusion_matrix(y_test, y_pred_svm)
sns.heatmap(
    conf_matrix,
    annot=True,
    fmt='d',
    cmap='YlOrRd',
    xticklabels=news_data.target_names,
    yticklabels=news_data.target_names,
    ax=ax2
)
ax2.set_title('SVM模型混淆矩阵', fontsize=16, fontweight='bold')
ax2.set_xlabel('预测类别', fontsize=12)
ax2.set_ylabel('真实类别', fontsize=12)
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')
print("已保存: confusion_matrix.png")

fig3, (ax3a, ax3b) = plt.subplots(1, 2, figsize=(14, 6))

feature_names = tfidf_extractor.get_feature_names_out()
top_n = 15

nb_feature_importance = np.exp(nb_model.feature_log_prob_[0])
top_indices_nb = np.argsort(nb_feature_importance)[-top_n:]
top_features_nb = [feature_names[i] for i in top_indices_nb]
top_scores_nb = nb_feature_importance[top_indices_nb]

ax3a.barh(range(len(top_features_nb)), top_scores_nb[-top_n:])
ax3a.set_yticks(range(len(top_features_nb)))
ax3a.set_yticklabels(top_features_nb[-top_n:])
ax3a.set_title('朴素贝叶斯 - 重要特征', fontsize=14)
ax3a.set_xlabel('特征重要性')

svm_coefficients = svm_model.coef_[0]
top_indices_svm = np.argsort(np.abs(svm_coefficients))[-top_n:]
top_features_svm = [feature_names[i] for i in top_indices_svm]
top_scores_svm = svm_coefficients[top_indices_svm]

colors = ['green' if x > 0 else 'red' for x in top_scores_svm]
ax3b.barh(range(len(top_features_svm)), top_scores_svm[-top_n:], color=colors)
ax3b.set_yticks(range(len(top_features_svm)))
ax3b.set_yticklabels(top_features_svm[-top_n:])
ax3b.set_title('SVM - 重要特征', fontsize=14)
ax3b.set_xlabel('特征权重')

plt.tight_layout()
plt.savefig('feature_importance.png', dpi=300, bbox_inches='tight')
print("已保存: feature_importance.png")

fig4, ax4 = plt.subplots(figsize=(8, 5))
models = ['朴素贝叶斯', '支持向量机']
accuracies = [nb_accuracy, svm_accuracy]
colors = ['skyblue', 'lightcoral']

bars = ax4.bar(models, accuracies, color=colors, edgecolor='black')
ax4.set_title('模型性能比较', fontsize=16, fontweight='bold')
ax4.set_ylabel('准确率', fontsize=12)
ax4.set_ylim(0, 1.0)

for bar, acc in zip(bars, accuracies):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width() / 2., height + 0.01,
             f'{acc:.3f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')
print("已保存: model_comparison.png")

try:
    from wordcloud import WordCloud

    print("\n8. 生成词云图...")

    all_text = ' '.join(df_news['cleaned_text'])

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        max_words=150,
        contour_width=1,
        contour_color='steelblue'
    ).generate(all_text)

    fig5, ax5 = plt.subplots(figsize=(12, 6))
    ax5.imshow(wordcloud, interpolation='bilinear')
    ax5.axis('off')
    ax5.set_title('新闻数据集词云', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('wordcloud.png', dpi=300, bbox_inches='tight')
    print("已保存: wordcloud.png")

except ImportError:
    print("注意: 未安装wordcloud库，跳过词云生成")

print("\n" + "=" * 60)
print("分析完成！结果总结")
print("=" * 60)
print(f"数据集: 20 Newsgroups (4个类别)")
print(f"总样本数: {len(df_news)}")
print(f"特征维度: {X_features.shape[1]}")
print(f"最佳模型: 线性支持向量机")
print(f"测试集准确率: {svm_accuracy:.4f}")
print(f"交叉验证平均准确率: {svm_cv_scores.mean():.4f}")
print(f"生成图表数: 4-5张")
print("=" * 60)

df_news.to_csv('processed_news_data.csv', index=False)
print("\n处理后的数据已保存至: processed_news_data.csv")