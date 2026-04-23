class BooksController < ApplicationController
  before_action :set_book, only: [:show, :edit, :update, :destroy]

  def index
    @books = Book.all
  end

  def show
  end

  def new
    @book = Book.new
  end

  def create
    @book = Book.new(book_params)
  
    if @book.save
      redirect_to books_path, notice: "Book created successfully"
    else
      render :new
    end
  end
  
  def edit
  end
  
  def destroy
    @book.destroy
    redirect_to books_path, notice: "Book deleted"
  end
  
  private
  
  def set_book
    @book = Book.find(params[:id])
  end
  
  def book_params
    params.require(:book).permit(:title, :author, :description, :price, :published_on, :genre)
  end
end
