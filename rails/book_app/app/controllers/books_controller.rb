class BooksController < ApplicationController
  before_action :set_book, only: [:show, :edit, :update, :destroy]

  def index
    @books = Book.order(created_at: :desc)

    if params[:query].present?
      @books = @books.where("title ILIKE ?", "%#{params[:query]}%")
    end
  end

  def show
    # @book is already set by before_action
  end

  def new
    @book = Book.new
  end

  def create
    @book = Book.new(book_params)
  
    if @book.save
      redirect_to @book, notice: "Book created successfully"
    else
      render :new
    end
  end
  
  def edit
    # @book is already set by before_action
  end

  def update
    if @book.update(book_params)
      redirect_to @book, notice: "Book updated successfully"
    else
      render :edit
    end
  end
  
  def destroy
    @book.destroy
    redirect_to books_path, notice: "Book deleted successfully"
  end
  
  private
  
  def set_book
    @book = Book.find(params[:id])
  end
  
  def book_params
    params.require(:book).permit(:title, :author, :description, :price, :published_on, :genre)
  end
end