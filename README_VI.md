# 📚 Book Seller AI - Hệ Thống Bán Sách Thông Minh

Hệ thống bán sách trực tuyến tích hợp AI với khả năng tìm kiếm thông minh, chatbot tư vấn và gợi ý sách cá nhân hóa.

## 🌟 Tính Năng Chính

### 🤖 Tính Năng AI

#### 1. **Chatbot Tư Vấn Sách Thông Minh**
- Tư vấn sách bằng tiếng Việt với AI chatbot
- Sử dụng mô hình AI từ Hugging Face (Meta-Llama-3, Mistral, Phi-3)
- Hệ thống fallback đa mô hình đảm bảo độ ổn định
- Tìm kiếm ngữ nghĩa (semantic search) để hiểu ý định người dùng
- Gợi ý sách dựa trên chủ đề, thể loại
- Định dạng câu trả lời theo Markdown với:
  - Mô tả về thể loại sách
  - Top 5 cuốn sách hay nhất thế giới
  - Sách hiện có tại cửa hàng
- Lọc câu hỏi ngoài chủ đề (off-topic detection)
- Gợi ý câu hỏi mẫu cho người dùng

#### 2. **Gợi Ý Sách Thông Minh (AI Recommendations)**
- Sử dụng embedding vectors (BAAI/bge-small-en-v1.5) để tính toán độ tương đồng
- Thuật toán hybrid scoring kết hợp:
  - **AI Similarity (60%)**: Độ tương đồng ngữ nghĩa qua cosine similarity
  - **Genre Match (20%)**: Khớp thể loại sách
  - **Price Range (10%)**: Khoảng giá tương đương
  - **Popularity (10%)**: Độ phổ biến (số lượng đã bán)
- Cache embedding trong 7 ngày để tối ưu hiệu suất
- Tự động cập nhật embedding khi nội dung sách thay đổi
- Gợi ý top 8 sách phù hợp nhất

#### 3. **Tìm Kiếm Nâng Cao (Enhanced Search)**
- **Fuzzy Search**: Tìm kiếm mờ với khả năng chịu lỗi chính tả
- **Synonym Support**: Hỗ trợ từ đồng nghĩa tiếng Việt/Anh
  - Tình yêu, lãng mạn, romance, love
  - Kinh tế, tài chính, business, finance
  - Tâm lý, psychology, cảm xúc
  - Và nhiều từ khóa khác...
- **Multi-field Search**: Tìm kiếm trên nhiều trường
  - Tiêu đề (title)
  - Tác giả (author)
  - Mô tả (description)
  - Nhà xuất bản (publisher)
- **Scoring Algorithm**: Thuật toán chấm điểm thông minh
  - Exact match (khớp chính xác)
  - String similarity (độ tương đồng chuỗi)
  - Levenshtein distance (khoảng cách chỉnh sửa)
  - Synonym matching (khớp từ đồng nghĩa)
- **Autocomplete**: Gợi ý tự động khi gõ

### 📖 Quản Lý Sách

#### Tính Năng CRUD Đầy Đủ
- **Thêm sách mới**
  - Upload nhiều ảnh (multi-image upload)
  - Tự động xử lý và tối ưu ảnh với Sharp
  - Tạo slug tự động từ tiêu đề
  - Phân loại theo xuất xứ và thể loại
- **Cập nhật thông tin sách**
  - Cập nhật thông tin cơ bản
  - Thêm/xóa ảnh
  - Tự động cập nhật slug khi đổi tiêu đề
- **Xóa sách**
  - Tự động xóa ảnh liên quan
- **Xem chi tiết sách**
  - Xem theo ID hoặc slug
  - Hiển thị đầy đủ thông tin và danh mục

#### Thông Tin Sách
- Tiêu đề, tác giả, nhà xuất bản
- ISBN (tùy chọn, unique)
- Mô tả chi tiết
- Giá bán
- Số lượng tồn kho
- Số lượng đã bán
- Hình ảnh (nhiều ảnh)
- Phân loại: Xuất xứ + Thể loại
- Slug (URL thân thiện SEO)

### 🛒 Quản Lý Đơn Hàng

#### Đặt Hàng
- **Guest Checkout**: Hỗ trợ đặt hàng không cần đăng nhập
- **Authenticated Checkout**: Đặt hàng cho người dùng đã đăng nhập
- Tự động cập nhật tồn kho và số lượng đã bán
- Lưu thông tin giao hàng
- Chọn phương thức thanh toán

#### Theo Dõi Đơn Hàng
- Xem danh sách đơn hàng của tôi
- Xem chi tiết đơn hàng
- Trạng thái đơn hàng:
  - Pending (Chờ xử lý)
  - Processing (Đang xử lý)
  - Shipped (Đã gửi hàng)
  - Delivered (Đã giao hàng)
  - Completed (Hoàn thành)
  - Cancelled (Đã hủy)
  - Returned (Đã trả hàng)
- Trạng thái thanh toán:
  - Pending (Chờ thanh toán)
  - Paid (Đã thanh toán)
  - Refunded (Đã hoàn tiền)

#### Quản Lý Đơn Hàng (Admin)
- Xem tất cả đơn hàng
- Cập nhật trạng thái đơn hàng
- Tự động cập nhật trạng thái thanh toán khi hoàn thành

### 👥 Quản Lý Người Dùng

#### Xác Thực & Phân Quyền
- **Đăng ký tài khoản**
  - Validation đầu vào (email, password, name)
  - Mã hóa mật khẩu với bcrypt
  - Tự động tạo JWT tokens
- **Đăng nhập**
  - Access Token (15 phút)
  - Refresh Token (7 ngày, HTTP-only cookie)
- **Refresh Token**
  - Tự động làm mới access token
- **Đăng xuất**
  - Xóa refresh token cookie
- **Phân quyền**
  - User (Người dùng)
  - Admin (Quản trị viên)

#### Quản Lý Hồ Sơ
- Xem thông tin cá nhân
- Cập nhật thông tin
- Đổi mật khẩu
- Xem lịch sử đơn hàng

#### Quản Lý User (Admin)
- Xem danh sách người dùng
- Cập nhật thông tin người dùng
- Phân quyền (user/admin)

### 📊 Thống Kê & Báo Cáo (Admin)

#### Dashboard
- **Tổng quan**
  - Tổng số sản phẩm
  - Tổng số đơn hàng
  - Tổng doanh thu
- **Đơn hàng gần đây**
  - 5 đơn hàng mới nhất

#### Biểu Đồ Doanh Thu
- Doanh thu theo ngày
- Lọc theo khoảng thời gian:
  - 7 ngày gần đây
  - 30 ngày gần đây

#### Top Sản Phẩm
- 10 sách bán chạy nhất
- Hiển thị số lượng đã bán

### 🎨 Quản Lý Nội Dung

#### Banner & Slider
- Tạo/sửa/xóa banner
- Upload ảnh banner
- Quản lý thứ tự hiển thị
- Bật/tắt banner

### 📂 Quản Lý Danh Mục

#### Xuất Xứ (Origin)
- Sách Việt Nam
- Sách nước ngoài
- Tạo/sửa/xóa danh mục xuất xứ

#### Thể Loại (Genres)
- Văn học
- Kinh tế
- Tâm lý
- Thiếu nhi
- Khoa học
- Lịch sử
- Và nhiều thể loại khác...
- Tạo/sửa/xóa thể loại
- Slug tự động cho SEO

### 🎫 Hỗ Trợ Khách Hàng

#### Yêu Cầu Hỗ Trợ
- **Loại yêu cầu**
  - Support (Hỗ trợ)
  - Return (Trả hàng)
- Gửi yêu cầu kèm:
  - Tiêu đề
  - Nội dung
  - Hình ảnh minh chứng
  - Liên kết đơn hàng (nếu có)
- Xem danh sách yêu cầu của tôi
- Theo dõi trạng thái:
  - Pending (Chờ xử lý)
  - In Progress (Đang xử lý)
  - Resolved (Đã giải quyết)

#### Quản Lý Hỗ Trợ (Admin)
- Xem tất cả yêu cầu
- Lọc theo loại và trạng thái
- Trả lời yêu cầu
- Cập nhật trạng thái
- Tự động cập nhật trạng thái đơn hàng khi chấp nhận trả hàng

### 📤 Upload & Xử Lý File

#### Upload Ảnh
- Upload nhiều ảnh cùng lúc
- Tự động tối ưu ảnh với Sharp
- Tạo 3 kích thước:
  - Small (300px)
  - Medium (600px)
  - Large (1200px)
- Hỗ trợ định dạng: JPG, PNG, WebP
- Giới hạn kích thước file
- Tự động xóa ảnh cũ khi cập nhật

## 🛠️ Công Nghệ Sử Dụng

### Backend
- **Node.js** + **Express.js**: Framework server
- **MongoDB** + **Mongoose**: Database & ODM
- **JWT**: Xác thực và phân quyền
- **Bcrypt**: Mã hóa mật khẩu
- **Multer**: Upload file
- **Sharp**: Xử lý ảnh
- **Helmet**: Bảo mật HTTP headers
- **CORS**: Cross-Origin Resource Sharing
- **Express Rate Limit**: Giới hạn request
- **Cookie Parser**: Xử lý cookies

### AI & Machine Learning
- **Hugging Face API**: Mô hình AI
  - Meta-Llama-3-8B-Instruct
  - Mistral-7B-Instruct-v0.2
  - Phi-3-mini-4k-instruct
- **BAAI/bge-small-en-v1.5**: Embedding model
- **Natural**: NLP library (Levenshtein distance)
- **String Similarity**: Tính toán độ tương đồng chuỗi

### Frontend
- **React 19**: UI framework
- **Vite**: Build tool
- **React Router DOM**: Routing
- **Axios**: HTTP client
- **TailwindCSS**: Styling
- **React Quill**: Rich text editor
- **React Dropzone**: File upload UI
- **Recharts**: Biểu đồ thống kê

## 📁 Cấu Trúc Dự Án

```
Book-Seller-AI/
├── client/                 # Frontend React
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── context/       # Context API
│   │   ├── utils/         # Utilities
│   │   └── App.jsx        # Main app
│   └── package.json
│
├── server/                # Backend Node.js
│   ├── config/           # Cấu hình
│   │   ├── db.js         # MongoDB connection
│   │   └── env.js        # Environment variables
│   ├── controllers/      # Business logic
│   │   ├── authController.js
│   │   ├── bookController.js
│   │   ├── chatController.js
│   │   ├── recommendationController.js
│   │   ├── searchController.js
│   │   ├── orderController.js
│   │   ├── userController.js
│   │   ├── categoryController.js
│   │   ├── supportController.js
│   │   ├── statsController.js
│   │   ├── contentController.js
│   │   └── uploadController.js
│   ├── models/           # Database models
│   │   ├── User.js
│   │   ├── Book.js
│   │   ├── BookEmbedding.js
│   │   ├── Order.js
│   │   ├── Category.js
│   │   ├── Support.js
│   │   ├── Content.js
│   │   ├── Cart.js
│   │   └── Notification.js
│   ├── routes/           # API routes
│   │   ├── authRoutes.js
│   │   ├── bookRoutes.js
│   │   ├── chatRoutes.js
│   │   ├── recommendationRoutes.js
│   │   ├── searchRoutes.js
│   │   ├── orderRoutes.js
│   │   ├── userRoutes.js
│   │   ├── categoryRoutes.js
│   │   ├── supportRoutes.js
│   │   ├── statsRoutes.js
│   │   ├── contentRoutes.js
│   │   └── uploadRoutes.js
│   ├── middleware/       # Middleware
│   │   ├── auth.js       # Authentication
│   │   ├── admin.js      # Admin authorization
│   │   └── errorHandler.js
│   ├── utils/            # Utilities
│   │   ├── generateToken.js
│   │   ├── validators.js
│   │   └── imageProcessor.js
│   ├── scripts/          # Database seeding
│   ├── uploads/          # Uploaded files
│   └── server.js         # Entry point
│
└── README_VI.md          # Tài liệu này
```

## 🚀 API Endpoints

### Authentication (`/api/auth`)
- `POST /register` - Đăng ký tài khoản
- `POST /login` - Đăng nhập
- `POST /refresh` - Làm mới access token
- `POST /logout` - Đăng xuất

### Users (`/api/user`)
- `GET /profile` - Xem hồ sơ (Private)
- `PUT /profile` - Cập nhật hồ sơ (Private)
- `PUT /change-password` - Đổi mật khẩu (Private)
- `GET /` - Danh sách user (Admin)
- `PUT /:id` - Cập nhật user (Admin)

### Books (`/api/books`)
- `GET /` - Danh sách sách (Public)
- `GET /:id` - Chi tiết sách theo ID (Public)
- `GET /slug/:slug` - Chi tiết sách theo slug (Public)
- `POST /` - Tạo sách mới (Admin)
- `PUT /:id` - Cập nhật sách (Admin)
- `DELETE /:id` - Xóa sách (Admin)
- `GET /suggest` - Gợi ý tự động (Public)

### AI Chat (`/api/chat`)
- `POST /` - Chat với AI về sách
- `GET /suggestions` - Gợi ý câu hỏi

### AI Recommendations (`/api/recommendations`)
- `GET /books/:bookId/ai-recommendations` - Gợi ý sách thông minh

### Search (`/api/search`)
- `GET /?q=<query>` - Tìm kiếm nâng cao
- `GET /suggest?q=<query>` - Autocomplete

### Orders (`/api/orders`)
- `POST /` - Tạo đơn hàng (Public/Private)
- `GET /my-orders` - Đơn hàng của tôi (Private)
- `GET /:id` - Chi tiết đơn hàng (Private)
- `GET /` - Tất cả đơn hàng (Admin)
- `PUT /:id/status` - Cập nhật trạng thái (Admin)

### Categories (`/api/categories`)
- `GET /origins` - Danh sách xuất xứ
- `GET /genres` - Danh sách thể loại
- `POST /origins` - Tạo xuất xứ (Admin)
- `POST /genres` - Tạo thể loại (Admin)
- `PUT /origins/:id` - Cập nhật xuất xứ (Admin)
- `PUT /genres/:id` - Cập nhật thể loại (Admin)
- `DELETE /origins/:id` - Xóa xuất xứ (Admin)
- `DELETE /genres/:id` - Xóa thể loại (Admin)

### Support (`/api/support`)
- `POST /` - Tạo yêu cầu hỗ trợ (Private)
- `GET /my` - Yêu cầu của tôi (Private)
- `GET /` - Tất cả yêu cầu (Admin)
- `PATCH /:id` - Cập nhật yêu cầu (Admin)

### Stats (`/api/stats`)
- `GET /dashboard` - Thống kê tổng quan (Admin)
- `GET /revenue` - Biểu đồ doanh thu (Admin)
- `GET /top-products` - Top sản phẩm (Admin)

### Content (`/api/content`)
- `GET /banners` - Danh sách banner
- `POST /banners` - Tạo banner (Admin)
- `PUT /banners/:id` - Cập nhật banner (Admin)
- `DELETE /banners/:id` - Xóa banner (Admin)

### Upload (`/api/upload`)
- `POST /image` - Upload ảnh (Admin)
- `POST /images` - Upload nhiều ảnh (Admin)

## ⚙️ Cài Đặt & Chạy Dự Án

### Yêu Cầu Hệ Thống
- Node.js >= 16.x
- MongoDB >= 5.x
- NPM hoặc Yarn

### Cài Đặt

#### 1. Clone Repository
```bash
git clone <repository-url>
cd Book-Seller-AI
```

#### 2. Cài Đặt Dependencies

**Backend:**
```bash
cd server
npm install
```

**Frontend:**
```bash
cd client
npm install
```

#### 3. Cấu Hình Environment Variables

Tạo file `.env` trong thư mục `server/`:

```env
# Server
NODE_ENV=development
PORT=5000

# Database
MONGO_URI=mongodb://localhost:27017/bookstore

# JWT
JWT_SECRET=your_jwt_secret_key_here
JWT_REFRESH_SECRET=your_refresh_secret_key_here

# Hugging Face API
HF_API_KEY=your_huggingface_api_key_here

# Client URL (for CORS)
CLIENT_URL=http://localhost:5173
```

#### 4. Khởi Chạy MongoDB
```bash
# Nếu dùng MongoDB local
mongod

# Hoặc dùng MongoDB Atlas (cloud)
# Cập nhật MONGO_URI trong .env
```

#### 5. Seed Database (Tùy chọn)
```bash
cd server
npm run seed:full
```

#### 6. Chạy Ứng Dụng

**Development Mode:**

Terminal 1 - Backend:
```bash
cd server
npm run dev
```

Terminal 2 - Frontend:
```bash
cd client
npm run dev
```

**Production Mode:**

Backend:
```bash
cd server
npm start
```

Frontend:
```bash
cd client
npm run build
npm run preview
```

### Truy Cập Ứng Dụng
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:5000
- **Health Check**: http://localhost:5000/health

## 🔑 Lấy Hugging Face API Key

1. Truy cập: https://huggingface.co/
2. Đăng ký/Đăng nhập tài khoản
3. Vào Settings → Access Tokens
4. Tạo token mới với quyền "Read"
5. Copy token và thêm vào file `.env`

## 📝 Ghi Chú Quan Trọng

### Bảo Mật
- Luôn sử dụng HTTPS trong production
- Không commit file `.env` lên Git
- Thay đổi JWT secrets trong production
- Sử dụng strong passwords
- Rate limiting đã được cấu hình (100 requests/15 phút)

### Hiệu Suất
- Embedding cache 7 ngày
- Image optimization tự động
- MongoDB indexing cho search
- Pagination cho danh sách

### AI Features
- Fallback system đảm bảo chatbot luôn hoạt động
- Retry mechanism cho API calls
- Timeout 10 giây cho AI requests
- Semantic search kết hợp fuzzy search

## 🐛 Troubleshooting

### Lỗi kết nối MongoDB
```bash
# Kiểm tra MongoDB đang chạy
mongod --version
# Kiểm tra connection string trong .env
```

### Lỗi Hugging Face API
```bash
# Kiểm tra API key
# Kiểm tra quota/rate limit
# Thử model khác trong fallback list
```

### Lỗi upload ảnh
```bash
# Kiểm tra thư mục uploads/ tồn tại
# Kiểm tra quyền ghi file
mkdir -p server/uploads/books
```

## 📄 License

ISC

## 👨‍💻 Tác Giả

Phát triển bởi đội ngũ Book Seller AI

## 🤝 Đóng Góp

Mọi đóng góp đều được chào đón! Vui lòng tạo Pull Request hoặc Issue.

---

**Chúc bạn sử dụng hệ thống thành công! 🎉**
