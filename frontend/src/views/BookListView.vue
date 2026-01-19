<template>
  <div class="books-grid">
    <el-card
      v-for="book in bookList"
      :key="book.id"
      class="book-card"
      shadow="hover"
      :body-style="{ padding: '12px' }"
      @click="handleCardClick(book.id)"
    >
      <div class="book-cover">
        <img
          :src="getBookCover(book)"
          :alt="book.title"
          class="cover-img"
        />
      </div>

      <div class="book-info">
        <div class="book-title">{{ book.title }}</div>
        <div class="book-author">{{ formatAuthors(book.authors) }}</div>
        <div class="book-meta">
          <span class="book-price">${{ book.price }}</span>
          <span class="book-publisher">{{ book.publisher }}</span>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import request from '@/utils/requests'

const bookList = ref([])

const getBookCover = (book) => {
  // 图片格式一： https://images.manning.com/172/216/resize/9781617296086.jpg
  // 图片格式二：https://images.manning.com/320/400/resize/9781617296086.jpg
  return `https://images.manning.com/320/400/resize/${book.image_url}`
}

const formatAuthors = (authors) => {
  if (!authors || !Array.isArray(authors)) return '未知作者'
  return authors.map((a) => a.name).join(', ')
}

const fetchBooks = async () => {
  try {
    const res = await request.get('/books/')
    bookList.value = res || []
  } catch (error) {
    console.error('请求失败：', error)
    bookList.value = []
  }
}

const handleCardClick = (bookId) => {
  console.log('点击了书籍:', bookId)
}

onMounted(() => {
  fetchBooks()
})
</script>

<style scoped>
.books-grid {
  display: grid;
  gap: 20px;
  padding: 20px;
  width: 100%;
  box-sizing: border-box;
  grid-template-columns: repeat(6, 1fr);
}

@media (max-width: 1400px) {
  .books-grid {
    grid-template-columns: repeat(5, 1fr);
  }
}

@media (max-width: 1200px) {
  .books-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (max-width: 900px) {
  .books-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    padding: 16px;
  }
}

@media (max-width: 600px) {
  .books-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    padding: 12px;
  }
}

@media (max-width: 400px) {
  .books-grid {
    grid-template-columns: 1fr;
  }
}

.book-card {
  cursor: pointer;
  border: 1px solid #ebeef5;
  border-radius: 8px;
  transition: all 0.25s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.book-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.book-cover {
  height: 174px;
  width: 139px;
  background: #f8f9fa;
  border-radius: 6px 6px 0 0;
  overflow: hidden;
  margin-bottom: 12px;
}

.cover-img {
  width: 100%;
  height: 100%;
  object-fit: fit;
  transition: transform 0.3s ease;
}

.book-card:hover .cover-img {
  transform: scale(1.03);
}

.book-info {
  padding: 0 4px 8px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.book-title {
  font-weight: 600;
  font-size: 14px;
  line-height: 1.4;
  color: #303133;
  margin-bottom: 8px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  min-height: 40px;
}

.book-author {
  font-size: 12px;
  color: #606266;
  margin-bottom: 12px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.book-meta {
  margin-top: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.book-price {
  font-size: 15px;
  font-weight: 700;
  color: #e6a23c;
}

.book-publisher {
  font-size: 11px;
  color: #909399;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

@media (max-width: 600px) {
  .book-title {
    font-size: 13px;
    min-height: 36px;
  }

  .book-price {
    font-size: 14px;
  }

  .book-cover {
    height: 150px;
  }
}
</style>
