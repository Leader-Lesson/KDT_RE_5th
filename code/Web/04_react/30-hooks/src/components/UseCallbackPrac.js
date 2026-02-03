import { useState, useCallback } from 'react';

// 코딩온 실습(hooks 강의)
export default function UseCallbackPrac() {
  const [items, setItems] = useState(['Item 1', 'Item 1', 'Item 3']);
  //   const [isEdit, setIsEdit] = useState(true);  // 이렇게 하면 클릭한 특정값 식별X
  const [editIndex, setEditIndex] = useState(null);
  const [editText, setEditText] = useState('');

  const handleEdit = useCallback((item, idx) => {
    console.log('handleEdit');
    setEditIndex(idx);
    setEditText(item);
  }, []);

  const handleSave = useCallback(() => {
    console.log('handleSave');
    setItems(items.map((item, idx) => (idx === editIndex ? editText : item)));
    setEditIndex(null);
  }, [editText]); // editText 변수의 값은 변경되는 값

  const handleDelete = useCallback(
    (targetIdx) => {
      console.log('handleDelete');
      setItems(items.filter((item, idx) => idx !== targetIdx));
    },
    [items] // items 에 변경사항이 생긴 뒤 삭제하려고 하면 동작X
  );

  return (
    <div>
      <ul>
        {items.map((item, idx) => {
          return (
            <li key={idx}>
              {editIndex === idx ? (
                <>
                  <input
                    type="text"
                    value={editText}
                    onChange={(e) => setEditText(e.target.value)}
                  />
                  <button onClick={handleSave}>Save</button>
                </>
              ) : (
                <>
                  {item}
                  <button onClick={() => handleEdit(item, idx)}>Edit</button>
                  <button onClick={() => handleDelete(idx)}>Delete</button>
                </>
              )}
            </li>
          );
        })}
      </ul>
    </div>
  );
}
