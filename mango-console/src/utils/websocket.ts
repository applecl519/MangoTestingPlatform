// WebSocketService.ts
import { reactive } from 'vue'
import { Notification } from '@arco-design/web-vue'

export const DRIVER = 'Mango Actuator'
export const SERVER = 'Mango Server'
export const WEB = 'mango-console'

interface WebSocketServiceState {
  url: string
  socket: WebSocket | null
}

export default class WebSocketService {
  private state: WebSocketServiceState

  constructor(url: string) {
    this.state = reactive({
      url,
      socket: null
    })
  }

  connect() {
    this.state.socket = new WebSocket(this.state.url)

    this.state.socket.onopen = () => {
      Notification.success(`Socket服务已启动，开始接收${SERVER}消息和发送指令给${DRIVER}！`)
      // 发送消息
      const message = {
        code: 200,
        func: null,
        user: null,
        msg: `Hi, ${SERVER}, mango-console Request Connection!`,
        data: null,
        end: null
      }
      this.state.socket?.send(JSON.stringify(message))
    }

    this.state.socket.onmessage = (event) => {
      const res = JSON.parse(event.data)
      Notification.info('Socket消息：' + res.msg)
    }

    this.state.socket.onclose = () => {
      Notification.error('Socket连接已关闭！')
    }

    this.state.socket.onerror = (error) => {
      console.log('Socket发生错误：', error)
    }
  }

  // 关闭函数
  disconnect() {
    if (this.state.socket) {
      this.state.socket.close()
      this.state.socket = null
    }
  }

  // 发送消息函数
  sendMessage(code: number, func: string, user: number, msg: string, data: object, end: boolean) {
    const message = {
      code: code,
      func: func,
      user: user,
      msg: msg,
      data: data,
      end: end
    }

    if (this.state.socket) {
      this.state.socket.send(JSON.stringify(message))
    }
  }
}
