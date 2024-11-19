# 学生管理系统前端

踩到的坑：

- Vue 的 `watchEffect` 和 React 的 `useEffect` 用法不同，需要慢慢适应
- 喜欢的组件库 [Fluent UI](https://react.fluentui.dev) 没有 Vue 版本，只能自己扒 CSS 下来
- 参照 [AI 的回答](https://chatgpt.com/share/673c7f4c-0dfc-8013-a8fe-bc4f5c750b84) 实现了自封装的 textarea 和 select 组件的双向绑定
- 前端和后端不在一个主机上，遇到跨域问题，参照[官方文档](https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware)解决