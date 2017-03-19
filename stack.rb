class Stack
  attr_accessor :data

  def intiialize(size = 10)
    @size = size
  end

  def data
    @data ||= []
  end

  def empty?
    top == -1
  end

  def full?
    data.length == @size
  end

  def add_top
    @top ||= -1
    @top += 1
  end

  def less_top
    @top ||= -1
    @top -= 1
  end

  def push(x)
    unless full?
      add_top
      data.push(x)
    else
      puts "Stack is Full"
    end
  end

  def pop
    unless empty?
      less_top
      data.pop
    else
      puts "Stack is empty"
    end
  end

end
