# 知识点：调用列表方法添加与删除元素，维护工具清单。

translation_requests = ['software manual', 'tourism brochure', 'research abstract', 'overnight legal brief']
print(translation_requests)

urgent_request = 'overnight legal brief'
translation_requests.remove(urgent_request)
print(translation_requests)
print(f"\nThe {urgent_request.title()} needs our team's immediate attention.")
