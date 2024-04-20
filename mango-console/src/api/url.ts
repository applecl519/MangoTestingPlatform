import { baseURL } from './axios.config'

export const baseAddress = baseURL

// 项目原始接口
export const updateUserInfo = '/updateUser'
export const addDepartment = '/addDepartment'
export const getCardList = '/getCardList'
export const getCommentList = '/getCommentList'

// 修改原始接口后的
export const login = '/login'
export const getMenuListByRoleId = '/menu/'
export const getAllMenuByRoleId = '/role'
export const getMenuList = '/menu_1'
export const test = '/config/test'
// -
export const userDepartmentList = '/user/project'
export const userUserLogs = '/user/user/logs'
export const userRoleList = '/user/role'
export const userAllRole = '/user/role/all'
export const userInfo = '/user/info'
export const userPassword = '/user/password'
export const userProjectAll = '/user/project/all'
export const userNickname = '/user/nickname'
export const userPutProject = '/user/project/put'
export const userEnvironment = '/user/environment'
export const userProjectEnvironment = '/user/project/environment'
export const userProjectModule = '/user/project/module'
export const userProjectModuleGetAll = '/user/project/module/get/all'
export const userFilesAllList = '/user/files/all/list'
export const userFilesUpload = '/user/files/upload'
export const userFilesDownload = '/user/files/download'
export const userFilesDelete = '/user/files/delete'

// -
export const apiInfo = '/api/info'
export const apiCaseInfoRun = '/api/case/api/info/run'
export const apiPutApiInfoType = '/api/put/api/info/type'
export const apiCopyInfo = '/api/copy/info'
export const apiCase = '/api/case'
export const apiCaseCody = '/api/case/copy'
export const apiCaseDetailed = '/api/case/detailed'
export const apiPutCaseSort = '/api/put/case/sort'
export const apiPutRefreshApiInfo = '/api/put/refresh/api/info'
export const apiPublic = '/api/public'
export const apiPublicPutStatus = '/api/public/put/status'
export const apiInfoName = '/api/info/name'
export const apiCaseSynchronous = '/api/case/synchronous'
export const apiCaseRun = '/api/case/run'
export const apiResult = '/api/result'
export const apiInfoResult = '/api/info/result'
export const apiResultWeek = '/api/result/week'
export const apiInfoCaseResult = '/api/info/result/case'
export const apiResultSuiteCase = '/api/result/suite/case'

// -
export const uiPage = '/ui/page'
export const uiPageName = '/ui/page/name'
export const uiPageCopy = '/ui/page/copy'
export const uiUiElement = '/ui/element'
export const uiUiElementTest = '/ui/element/test'
export const uiUiElementPutIsIframe = '/ui/element/put/is/iframe'
export const uiUiElementName = '/ui/element/name'
export const uiSteps = '/ui/steps'
export const uiStepsPageStepsName = '/ui/steps/page/steps/name'
export const uiCase = '/ui/case'
export const uiCaseRun = '/ui/case/run'
export const uiCaseCopy = '/ui/case/copy/case'
export const uiCaseStepsDetailed = '/ui/case/steps/detailed'
export const uiCaseStepsRefreshCacheData = '/ui/case/steps/refresh/cache/data'
export const uiPageStepsDetailed = '/ui/page/steps/detailed'
export const uiStepsPutType = '/ui/steps/put/type'
export const uiPageStepsCopy = '/ui/copy/page/steps'
export const uiPageStepsDetailedAss = '/ui/page/steps/detailed/ass'
export const uiPageStepsDetailedOpe = '/ui/page/steps/detailed/ope'
export const uiPageAssMethod = '/ui/page/ass/method'
export const uiPagePutStepSort = '/ui/page/put/step/sort'
export const uiStepsRun = '/ui/steps/run'
export const uiRunCaseBatch = 'ui/case/batch/run'
export const uiConfig = '/ui/config'
export const uiConfigPutStatus = '/ui/config/put/status'
export const uiConfigNewBrowserObj = '/ui/config/new/browser/obj'
export const uiCaseNane = '/ui/case/name'
export const uiPublic = '/ui/public'
export const uiPublicPutStatus = '/ui/public/put/status'
export const uiCaseResultSuiteGetCase = '/ui/case/result/suite/get/case'
export const uiCasePutCaseSort = '/ui/case/put/case/sort'
export const uiEleResultEle = '/ui/ele/result/ele'
export const uiCaseResultWeekSum = '/ui/result/week'

// -
export const systemTestObject = '/system/test/object'
export const systemTestObjName = '/system/test/obj/name'
export const systemNotice = '/system/notice'
export const systemNoticePutStatus = '/system/notice/put/status'
export const systemDatabase = '/system/database'
export const systemTestObjectPutStatus = '/system/test/object/put/status'
export const systemRandomList = 'system/variable/random/list'
export const systemRandomData = 'system/variable/value'
export const systemTime = 'system/time'
export const systemTriggerTiming = 'system/trigger/timing'
export const systemScheduledTasks = 'system/scheduled/tasks'
export const systemScheduledPutStatus = 'system/scheduled/put/status'
export const systemScheduledPutNotice = 'system/scheduled/put/notice'
export const systemScheduledName = 'system/scheduled/name'
export const systemTasksRunCase = 'system/tasks/run/case'
export const systemTasksTypeCaseName = 'system/tasks/type/case/name'
export const systemTasksBatchSetCases = 'system/tasks/batch/set/cases'
export const systemSocketUserList = 'system/socket/user/list'
export const systemSocketAllUserSum = 'system/socket/all/user/sum'
export const systemTimingList = 'system/get/timing/list'
export const systemNoticeTest = 'system/notice/test'
export const systemTestSuiteReport = 'system/test/suite/report'
export const systemTasksCaseSort = 'system/tasks/case/sort'
export const systemTasksCaseTestObject = 'system/tasks/case/test/object'
export const systemTest = 'system/test'

export const systemCaseSum = 'system/case/sum'
export const systemCaseRunSum = 'system/case/run/sum'
export const systemCaseResultWeekSum = 'system/case/result/week/sum'
export const systemActivityLevel = 'system/activity/level'
export const systemCacheKeyValue = 'system/cache/key/value'
export const systemCacheData = 'system/cache/data'
export const systemEnumClient = 'system/enum/client'
export const systemEnumMethod = 'system/enum/method'
export const systemEnumApiPublic = 'system/enum/api/public'
export const systemEnumEnd = 'system/enum/end'
export const systemEnumNotice = 'system/enum/notice'
export const systemEnumStatus = 'system/enum/status'
export const systemEnumEnvironment = 'system/enum/environment'
export const systemEnumPlatform = 'system/enum/platform'
export const systemEnumBrowser = 'system/enum/browser'
export const systemEnumDrive = 'system/enum/drive'
export const systemEnumExp = 'system/enum/exp'
export const systemEnumAutotest = 'system/enum/autotest'
export const systemEnumCaseLevel = 'system/enum/case/level'
export const systemEnumUiPublic = 'system/enum/ui/public'
export const systemEnumUiElementOperation = 'system/enum/ui/element/operation'
export const systemEnumApiParameterType = 'system/enum/api/parameter/type'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $urlPath: Record<string, string>
  }
}
