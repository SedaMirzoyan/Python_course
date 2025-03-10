#ifndef LIST_H
#define LIST_H

template <typename T>
struct Node {
	Node* next;
	T val;

	Node()
	{
		std::cout << __func__ << std::endl;
		this->next = nullptr;
		this->val = 0;
	}

	Node(T elem)
	{
		std::cout << __func__ << std::endl;
		this->next = nullptr;
		this->val = elem;
	}

	~Node()
	{
		std::cout << __func__ << std::endl;
	}
};


template <typename T>
class List {
private:
	Node<T>* m_head;
	Node<T>* m_tail;
	int m_length;

public:
	List();
	List(const T& elem);
	~List();

public:
	Node<T>* createNode(const T& elem);
	void insertAtBeginning(const T& elem);
	void insertAtIndex(const T& elem, int index);
	void insertAtEnd(const T& elem);
	void print();
	int getLength()const;
	void setLength(int l);
	void removeFromEnd();
	void removeFromBeginning();
	void removeAtIndex(int index);
	T getLastElem()const;
};

template <typename T>
List<T>::List()
{
	std::cout << __func__ << std::endl;
	m_head = nullptr;
	m_tail = nullptr;

	m_length = 0;
}

template <typename T>
List<T>::List(const T& elem)
{
	std::cout << __func__ << std::endl;
	m_head = new Node<T>(elem);
	m_tail = new Node<T>(elem);

	m_length = m_length++;
}

template <typename T>
List<T>::~List()
{
	std::cout << __func__ << std::endl;
}


template <typename T>
void List<T>::setLength(int l)
{
	if (l < 0)
	{
		std::cout << "size can't be negative\n";
	}
	m_length = l;
}


template <typename T>
int List<T>::getLength()const
{
	return m_length;
}


template <typename T>
Node<T>* List<T>::createNode(const T& elem)
{
	Node<T>* new_node = new Node<T>;
	if (m_head == nullptr)
	{
		m_head = new_node;
		m_head->next = new_node;
		m_head->val = elem;
		m_tail = m_head;
	}
	return new_node;
}


template <typename T>
void List<T>::insertAtBeginning(const T& elem)
{
	Node<T>* new_node = createNode(elem);

	new_node->next = m_head;
	new_node->val = elem;
	m_head = new_node;
	m_length++;
}

template <typename T>
void List<T>::insertAtEnd(const T& elem)
{
	Node<T>* new_node = createNode(elem);

	m_tail->next = new_node;
	m_tail = new_node;
	m_tail->next = nullptr;
	new_node->val = elem;
	m_length++;
}


template <typename T>
void List<T>::insertAtIndex(const T& elem, int index)
{
	Node<T>* new_node = createNode(elem);

	int prev_index = index - 1;
	Node<T>* prev = m_head;

	for (int i = 0; i < prev_index; i++)
	{
		prev = prev->next;
	}

	new_node->next = prev->next;
	prev->next = new_node;
	new_node->val = elem;
	m_length++;
}


template <typename T>
void List<T>::removeFromBeginning()
{
	if (m_length == 0)
	{
		std::cout << "Nothing to delete, list is empty\n";
	}
	Node<T>* tmp = m_head;

	m_head = m_head->next;
	tmp->next = nullptr;
	tmp = nullptr;
	m_length--;
}

template <typename T>
void List<T>::removeAtIndex(int index)
{
	if (m_length == 0)
	{
		std::cout << "Nothing to delete, list is empty\n";
	}

	Node<T>* tmp = m_head;
	for (int i = 0; i < index; i++)
	{
		tmp = tmp->next;
	}

	int prev_index = index - 1;
	Node<T>* prev = m_head;
	for (int i = 0; i < prev_index; i++)
	{
		prev = prev->next;
	}

	prev->next = tmp->next;
	tmp->next = nullptr;
	m_length--;
}



template <typename T>
void List<T>::removeFromEnd()
{
	if (m_length == 0)
	{
		std::cout << "Nothing to delete, list is empty\n";
	}
	Node<T>* tmp = m_head;
	Node<T>* prev = m_head;

	for (int i = 0; i < m_length - 1; i++)
	{
		prev = tmp;
		tmp = tmp->next;
	}

	m_tail = prev;
	m_tail->next = prev->next;
	tmp->next = nullptr;
	prev->next = nullptr;
	m_length--;
}


template <typename T>
void List<T>::print()
{
	Node<T>* tmp = m_head;
	while (tmp != nullptr)
	{
		std::cout << tmp->val << " ";
		tmp = tmp->next;
	}
	std::cout << std::endl;
}


template <typename T>
T List<T>::getLastElem()const
{
	return m_tail->val;
}

#endif //LIST_H



