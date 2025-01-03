import '../styles/transition.css'
import { App, inject } from 'vue'
import { TinyEmitter } from 'tiny-emitter'

import { toHump } from '../utils'
import components from '../components'

import ArcoVueIcon from '@arco-design/web-vue/es/icon'
import '@arco-design/web-vue/dist/arco.css'
import ArcoVue from '@arco-design/web-vue/es/arco-vue'

function getComponentName(key: string) {
  if (!key) {
    return ''
  }
  const paths = key.split('/')
  const name = paths
    .filter((it) => !!it && it !== '.')
    .reverse()
    .find(
      (it) =>
        it !== 'index.vue' &&
        it !== 'user.ts' &&
        it !== 'index.js' &&
        it !== 'index.jsx' &&
        it !== 'index.tsx'
    )
    ?.replace('.vue', '')
    ?.replace('.tsx', '')
  return name || ''
}

export function registerComponents(app: App) {
  const components = import.meta.globEager('./**/**.{vue,tsx}')
  Object.keys({ ...components }).forEach((it: string) => {
    const component = components[it]
    app.component(component.default.name || toHump(getComponentName(it)), component.default)
  })
}

export const emitKey = Symbol('tiny-emit')

function install(app: App) {
  app.use(ArcoVue)
  app.use(ArcoVueIcon)
  registerComponents(app)
  app.use(components, { getComponentName })
  app.provide(emitKey, new TinyEmitter())
}

export function setupGlobalComponent(app: App) {
  install(app)
}
